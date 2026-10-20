# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 11:58:24 2026

@author: wk1n25
"""
import pandas as pd
from IPython.display import display, HTML
from pathlib import Path

OUTPUT_TYPE_NAMES = {
    "A": "Authored book",
    "B": "Edited book",
    "C": "Chapter in book",
    "D": "Journal article",
    "E": "Conference contribution",
    "F": "Patent or published patent application",
    "G": "Software",
    "H": "Website content",
    "I": "Performance",
    "J": "Composition",
    "K": "Design",
    "L": "Artefact",
    "M": "Exhibition",
    "N": "Research report for external body",
    "P": "Devices and products",
    "Q": "Digital or visual media",
    "R": "Scholarly edition",
    "S": "Research data sets and databases",
    "T": "Other",
    "U": "Working paper",
    "V": "Translation",
}

file_name = '../data/REF2021/ref2021_submissions_full.csv'

df = pd.read_csv(file_name)
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

df = df.rename(columns={'unit_of_assessment_number':'uoa_number', 'output_type': 'output'})

#look for portfolios based on the 'contextual information' phrase
df_portfolios = df.loc[df['publisher'].fillna('').str.contains(r'contextual(?:ising)*\s+information', case=False, regex=True) | 
                       df['title'].fillna('').str.contains(r'contextual(?:ising)*\s+information', case=False, regex=True)]

by_uoa = df_portfolios.groupby('uoa_number').count()['ID']
df_portfolios.groupby('uoa').count()
by_panel = df_portfolios.groupby('main_panel').count()
by_output_type = df_portfolios.groupby(['output', 'uoa', 'uoa_number', 'main_panel']).count()['ID']

# look for portfolios based on the 'multi-component' phrase
df_multi = df.loc[(df['publisher'].fillna('').str.contains(r'multi[\s-]*component', case=False, regex=True) & 
                 ~df['publisher'].fillna('').str.contains(r'contextual(?:ising)*\s+information', case=False, regex=True)) |
                  (df['title'].fillna('').str.contains(r'multi[\s-]*component', case=False, regex=True) & 
                 ~df['title'].fillna('').str.contains(r'contextual(?:ising)*\s+information', case=False, regex=True))]

#portfolios based on both phrases
df_both_portfolio = df.loc[df['publisher'].fillna('').str.contains(r'multi[\s-]*component', case=False, regex=True) | 
                 df['publisher'].fillna('').str.contains(r'contextual(?:ising)*\s+information', case=False, regex=True) |
                  df['title'].fillna('').str.contains(r'multi[\s-]*component', case=False, regex=True) | 
                 df['title'].fillna('').str.contains(r'contextual(?:ising)*\s+information', case=False, regex=True)]

# Portfolios do not have a volume title
df_both_portfolio = df_both_portfolio.loc[df_both_portfolio['volume_title'].isna()]

df_both_portfolio['output_name'] = (
    df_both_portfolio['output']
    .map(OUTPUT_TYPE_NAMES))

both_by_output_type = (
    df_both_portfolio
    .groupby(['output', 'output_name', 'uoa', 'uoa_number', 'main_panel', 'institution'])
    .size()
    .rename('count')
    .to_frame()
    .sort_values(by='count', ascending=False)
    .sort_index(level=['output', 'main_panel', 'uoa_number'], sort_remaining=False))

# Creating a more concise table for Readme
table_with_totals = (
    df_both_portfolio
    .groupby(['output', 'output_name', 'uoa', 'uoa_number', 'main_panel'])
    .size()
    .rename('count')
    .to_frame()
    .sort_values(by='count', ascending=False)
    .sort_index(level=[ 'main_panel', 'output'], sort_remaining=False))

# Getting totals
table_with_totals['panel_total'] = (
    table_with_totals
    .groupby(level='main_panel')['count']
    .transform('sum')
)

table_with_totals['output_total'] = (
    table_with_totals
    .groupby(level='output')['count']
    .transform('sum')
)

# Setting totals as indexes and reordering
table_with_totals = (
    table_with_totals
    .set_index('panel_total', append=True)
    .set_index('output_total', append=True)
    .reorder_levels(['main_panel', 'panel_total','output', 'output_name', 
                     'output_total',  'uoa_number', 'uoa'])
)

#both_by_output_type.plot(kind='barh')

df_portfolio_direct = df.loc[df['publisher'].fillna('').str.contains(r'portfolio', case=False, regex=True) | 
                       df['title'].fillna('').str.contains(r'portfolio', case=False, regex=True)]

#display(HTML(both_by_output_type.to_html()))
both_by_output_type.to_html("table.html")

# Update the README.md file to include the summary table

table = both_by_output_type.reset_index().to_markdown(index=False)

readme_path = Path("README.md")
readme = readme_path.read_text(encoding="utf-8")

start = "<!-- TABLE_START -->"
end = "<!-- TABLE_END -->"

before = readme.split(start)[0]
after = readme.split(end)[1]

new_readme = (
    before
    + start
    + '\n Total portfolios found: ' + str(table_with_totals.sum().iloc[0])
    + "\n\n"
    + '<table>'
    + table_with_totals.to_html().replace('_', ' ')
    + '<\\table>'
    + "\n\n"
    + end
    + after
)

readme_path.write_text(new_readme, encoding="utf-8")
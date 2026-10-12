# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 11:58:24 2026

@author: wk1n25
"""
import pandas as pd
from IPython.display import display, HTML

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

#look for portfolios based on the 'contextual information' phrase
df_portfolios = df.loc[df['publisher'].fillna('').str.contains(r'contextual\s+information', case=False, regex=True) | 
                       df['title'].fillna('').str.contains(r'contextual\s+information', case=False, regex=True)]

by_uoa = df_portfolios.groupby('unit_of_assessment_number').count()['ID']
df_portfolios.groupby('uoa').count()
by_panel = df_portfolios.groupby('main_panel').count()
by_output_type = df_portfolios.groupby(['output_type', 'uoa', 'unit_of_assessment_number', 'main_panel']).count()['ID']

# look for portfolios based on the 'multi-component' phrase
df_multi = df.loc[(df['publisher'].fillna('').str.contains(r'multi\s+component', case=False, regex=True) & 
                 ~df['publisher'].fillna('').str.contains(r'contextual\s+information', case=False, regex=True)) |
                  (df['title'].fillna('').str.contains(r'multi\s+component', case=False, regex=True) & 
                 ~df['title'].fillna('').str.contains(r'contextual\s+information', case=False, regex=True))]

#portfolios based on both phrases
df_both_portfolio = df.loc[df['publisher'].fillna('').str.contains(r'multi\s+component', case=False, regex=True) | 
                 df['publisher'].fillna('').str.contains(r'contextual\s+information', case=False, regex=True) |
                  df['title'].fillna('').str.contains(r'multi\s+component', case=False, regex=True) | 
                 df['title'].fillna('').str.contains(r'contextual\s+information', case=False, regex=True)]

df_both_portfolio=df_both_portfolio.loc[df_both_portfolio['output_type']!='D']

both_by_output_type = (
    df_both_portfolio
    .groupby(['output_type', 'uoa', 'unit_of_assessment_number', 'main_panel', 'institution'])
    .size()
    .rename('count')
    .to_frame()
    .sort_index(level='output_type'))

both_by_output_type['output_type_name'] = (
    both_by_output_type.index.get_level_values('output_type')
    .map(OUTPUT_TYPE_NAMES))

#both_by_output_type.plot(kind='barh')

df_portfolio_direct = df.loc[df['publisher'].fillna('').str.contains(r'portfolio', case=False, regex=True) | 
                       df['title'].fillna('').str.contains(r'portfolio', case=False, regex=True)]

#display(HTML(both_by_output_type.to_html()))
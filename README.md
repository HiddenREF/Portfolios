# Identifying portfolios submitted to REF2021

In REF2021, a portfolio was not a category of output type in [Annex K: Output glossary and collection formats](https://www.britsoc.co.uk/media/24852/annex-k-output-glossary-and-collection-formats.pdf). Portfolios were nevertheless submitted to REF2021 as outputs of research, 'hidden' within existing output categories. There is not easy way, therefore, of identifying portfolios submitted as outputs to REF2021 and calculating their volume and distribution relative to other output types. This repository provides a reproducible way of identifying portfolios, based on terminology in the REF guidance and information retained in the published output metadata, as a basis for calculating their volume and distribution. Any portfolios submitted that **did not** use the terminology in the REF guidance as part of their submission will not be found by this approach.

## Which outputs are portfolios?

This repository explores how portfolio-style submissions can be identified in the published REF2021 output metadata.

The approach is based on the terminology provided by the REF2021 guidance for use in title or publisher fields during submission of outputs. See the REF2021 [Panel criteria and working methods](https://2021.ref.ac.uk/media/1450/ref-2019_02-panel-criteria-and-working-methods.pdf), and [Submitting practice research outputs to REF2021](https://2021.ref.ac.uk/media/1238/submitting-practice-research-outputs-to-ref2021.pdf).

In particular, the terms..

- `"Multi-component"`
- `"contextual information"`

.. (and their variant forms, including `"Multi component"`, `"multicomponent"`, and `"contextualising information"`) appear to provide the most useful indicators of an output that is structured as a portfolio.

The script [find_group_portfolios.py](https://github.com/HiddenREF/Portfolios/blob/main/find_group_portfolios.py) searches REF output metadata for these indicators, including their occurrence in fields such as **title** and **publisher**.

> ## Important limitation
>**The metadata may not capture every portfolio-style submission.**  
>   The method can therefore identify likely portfolios where relevant terminology is present, but should not be interpreted as establishing that outputs without those terms were not portfolios.

## Results

We have grouped the matching records by:

- REF output type,
- Main Panel,
- Unit of Assessment (UOA) number, and
- Count.

The results are shown below.

<!-- TABLE_START -->
 Total portfolios found: 504

<table><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th>count</th>
    </tr>
    <tr>
      <th>main panel</th>
      <th>panel total</th>
      <th>output</th>
      <th>output name</th>
      <th>output total</th>
      <th>uoa number</th>
      <th>uoa</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">C</th>
      <th rowspan="2" valign="top">3</th>
      <th rowspan="2" valign="top">T</th>
      <th rowspan="2" valign="top">Other</th>
      <th rowspan="2" valign="top">365</th>
      <th>22</th>
      <th>Anthropology and Development Studies</th>
      <td>2</td>
    </tr>
    <tr>
      <th>14</th>
      <th>Geography and Environmental Studies</th>
      <td>1</td>
    </tr>
    <tr>
      <th rowspan="21" valign="top">D</th>
      <th rowspan="21" valign="top">501</th>
      <th rowspan="2" valign="top">H</th>
      <th rowspan="2" valign="top">Website content</th>
      <th rowspan="2" valign="top">3</th>
      <th>33</th>
      <th>Music, Drama, Dance, Performing Arts, Film and Screen Studies</th>
      <td>2</td>
    </tr>
    <tr>
      <th>32</th>
      <th>Art and Design: History, Practice and Theory</th>
      <td>1</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">I</th>
      <th rowspan="3" valign="top">Performance</th>
      <th rowspan="3" valign="top">24</th>
      <th>33</th>
      <th>Music, Drama, Dance, Performing Arts, Film and Screen Studies</th>
      <td>14</td>
    </tr>
    <tr>
      <th>32</th>
      <th>Art and Design: History, Practice and Theory</th>
      <td>9</td>
    </tr>
    <tr>
      <th>27</th>
      <th>English Language and Literature</th>
      <td>1</td>
    </tr>
    <tr>
      <th>J</th>
      <th>Composition</th>
      <th>42</th>
      <th>33</th>
      <th>Music, Drama, Dance, Performing Arts, Film and Screen Studies</th>
      <td>42</td>
    </tr>
    <tr>
      <th>K</th>
      <th>Design</th>
      <th>3</th>
      <th>32</th>
      <th>Art and Design: History, Practice and Theory</th>
      <td>3</td>
    </tr>
    <tr>
      <th>L</th>
      <th>Artefact</th>
      <th>8</th>
      <th>32</th>
      <th>Art and Design: History, Practice and Theory</th>
      <td>8</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">M</th>
      <th rowspan="4" valign="top">Exhibition</th>
      <th rowspan="4" valign="top">34</th>
      <th>32</th>
      <th>Art and Design: History, Practice and Theory</th>
      <td>30</td>
    </tr>
    <tr>
      <th>34</th>
      <th>Communication, Cultural and Media Studies, Library and Information Management</th>
      <td>2</td>
    </tr>
    <tr>
      <th>28</th>
      <th>History</th>
      <td>1</td>
    </tr>
    <tr>
      <th>33</th>
      <th>Music, Drama, Dance, Performing Arts, Film and Screen Studies</th>
      <td>1</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Q</th>
      <th rowspan="4" valign="top">Digital or visual media</th>
      <th rowspan="4" valign="top">24</th>
      <th>34</th>
      <th>Communication, Cultural and Media Studies, Library and Information Management</th>
      <td>13</td>
    </tr>
    <tr>
      <th>32</th>
      <th>Art and Design: History, Practice and Theory</th>
      <td>8</td>
    </tr>
    <tr>
      <th>33</th>
      <th>Music, Drama, Dance, Performing Arts, Film and Screen Studies</th>
      <td>2</td>
    </tr>
    <tr>
      <th>27</th>
      <th>English Language and Literature</th>
      <td>1</td>
    </tr>
    <tr>
      <th>S</th>
      <th>Research data sets and databases</th>
      <th>1</th>
      <th>26</th>
      <th>Modern Languages and Linguistics</th>
      <td>1</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">T</th>
      <th rowspan="4" valign="top">Other</th>
      <th rowspan="4" valign="top">365</th>
      <th>32</th>
      <th>Art and Design: History, Practice and Theory</th>
      <td>263</td>
    </tr>
    <tr>
      <th>33</th>
      <th>Music, Drama, Dance, Performing Arts, Film and Screen Studies</th>
      <td>73</td>
    </tr>
    <tr>
      <th>34</th>
      <th>Communication, Cultural and Media Studies, Library and Information Management</th>
      <td>17</td>
    </tr>
    <tr>
      <th>27</th>
      <th>English Language and Literature</th>
      <td>9</td>
    </tr>
  </tbody>
</table><\table>

<!-- TABLE_END -->


## REF2021 guidance

The methodology is based on the following official REF2021 guidance:

- **[Panel criteria and working methods (REF 2019/02)](https://2021.ref.ac.uk/media/1450/ref-2019_02-panel-criteria-and-working-methods.pdf)**  
  See in particular page 48.

- **[Submitting practice research outputs to REF2021](https://2021.ref.ac.uk/media/1238/submitting-practice-research-outputs-to-ref2021.pdf)**  


## Reference

Suggested reference:

-  Wioleta Kijewska, James Baker, Simon Hettrick, Lyndsey Ballantyne, Michael Donnay, Gemma Derrick, Ben Thomas, and Ola Thomson, *Identifying portfolios submitted to REF2021* (The Hidden REF, 2026) [https://github.com/HiddenREF/Portfolios](https://github.com/HiddenREF/Portfolios)


### Files

- `table.html` – the results table in a .html format.
- `find_group_portfolios.py` – Python script that finds and groups the portfolio submissions.

#### Running script
The script requires the `ref2021_submissions_full.csv` datafile with all REF2021 submissions, and uses libraries `pandas`, `pathlib`, and `IPython.display`. The script will update the README.md file with the current view of the results table.


# Identifying portfolios submitted to REF2021

In REF2021, a portfolio was not a category of output type in [Annex K: Output glossary and collection formats](https://www.britsoc.co.uk/media/24852/annex-k-output-glossary-and-collection-formats.pdf). Portfolios were nevertheless submitted to REF2021 as outputs of research, 'hidden' within existing output categories. There is not easy way, therefore, of identifying portfolios submitted as outputs to REF2021 and calculating their volume and distribution relative to other output types. This repository provides a reproducible way of identifying portfolios, based on terminology in the REF guidance and information retained in the published output metadata, as a basis for calculating their volume and distribution. Any portfolios submitted that **did not** use the terminology in the REF guidance as part of their submission will not be found by this approach.

## Which outputs are portfolios?

This repository explores how portfolio-style submissions can be identified in the published REF2021 output metadata.

The approach is based on the terminology used in the REF2021 guidance. See the REF2021 [Panel criteria and working methods](https://2021.ref.ac.uk/media/1450/ref-2019_02-panel-criteria-and-working-methods.pdf), and [Submitting practice research outputs to REF2021](https://2021.ref.ac.uk/media/1238/submitting-practice-research-outputs-to-ref2021.pdf).

In particular, the terms:

- `"Multi-component"`
- `"contextual information"`

appear to provide the most useful indicators of an output that is structured as a portfolio.

The script [find_group_portfolios.py](https://github.com/HiddenREF/Portfolios/blob/main/find_group_portfolios.py) searches REF output metadata for these indicators, including their occurrence in fields such as **title** and **publisher**.

> ## Important limitation
>**The metadata may not capture every portfolio-style submission.**  
>   The method can therefore identify likely portfolios where relevant terminology is present, but should not be interpreted as establishing that outputs without those terms were not portfolios.

## Results

We have grouped the matching records by:

- REF output type,
- Unit of Assessment (UOA),
- Main Panel, and
- Submitting institution.

The results are shown below.

<!-- TABLE_START -->

| output   | output_name                      | uoa                                                                           |   uoa_number | main_panel   | institution                                           |   count |
|:---------|:---------------------------------|:------------------------------------------------------------------------------|-------------:|:-------------|:------------------------------------------------------|--------:|
| H        | Website content                  | Art and Design: History, Practice and Theory                                  |           32 | D            | Bournemouth University                                |       1 |
| H        | Website content                  | Music, Drama, Dance, Performing Arts, Film and Screen Studies                 |           33 | D            | Bath Spa University                                   |       2 |
| I        | Performance                      | Art and Design: History, Practice and Theory                                  |           32 | D            | Bath Spa University                                   |       9 |
| I        | Performance                      | English Language and Literature                                               |           27 | D            | University of Cambridge                               |       1 |
| I        | Performance                      | Music, Drama, Dance, Performing Arts, Film and Screen Studies                 |           33 | D            | Bath Spa University                                   |       6 |
| I        | Performance                      | Music, Drama, Dance, Performing Arts, Film and Screen Studies                 |           33 | D            | City, University of London                            |       2 |
| I        | Performance                      | Music, Drama, Dance, Performing Arts, Film and Screen Studies                 |           33 | D            | Edinburgh Napier University                           |       1 |
| I        | Performance                      | Music, Drama, Dance, Performing Arts, Film and Screen Studies                 |           33 | D            | Guildhall School of Music & Drama                     |       5 |
| J        | Composition                      | Music, Drama, Dance, Performing Arts, Film and Screen Studies                 |           33 | D            | Bath Spa University                                   |      17 |
| J        | Composition                      | Music, Drama, Dance, Performing Arts, Film and Screen Studies                 |           33 | D            | City, University of London                            |       4 |
| J        | Composition                      | Music, Drama, Dance, Performing Arts, Film and Screen Studies                 |           33 | D            | De Montfort University                                |       1 |
| J        | Composition                      | Music, Drama, Dance, Performing Arts, Film and Screen Studies                 |           33 | D            | Edinburgh Napier University                           |       6 |
| J        | Composition                      | Music, Drama, Dance, Performing Arts, Film and Screen Studies                 |           33 | D            | Guildhall School of Music & Drama                     |      13 |
| J        | Composition                      | Music, Drama, Dance, Performing Arts, Film and Screen Studies                 |           33 | D            | The University of West London                         |       1 |
| K        | Design                           | Art and Design: History, Practice and Theory                                  |           32 | D            | Anglia Ruskin University Higher Education Corporation |       1 |
| K        | Design                           | Art and Design: History, Practice and Theory                                  |           32 | D            | Bath Spa University                                   |       2 |
| L        | Artefact                         | Art and Design: History, Practice and Theory                                  |           32 | D            | Bath Spa University                                   |       5 |
| L        | Artefact                         | Art and Design: History, Practice and Theory                                  |           32 | D            | Bournemouth University                                |       1 |
| L        | Artefact                         | Art and Design: History, Practice and Theory                                  |           32 | D            | Staffordshire University                              |       1 |
| L        | Artefact                         | Art and Design: History, Practice and Theory                                  |           32 | D            | University of Chester                                 |       1 |
| M        | Exhibition                       | Art and Design: History, Practice and Theory                                  |           32 | D            | Bath Spa University                                   |      29 |
| M        | Exhibition                       | Art and Design: History, Practice and Theory                                  |           32 | D            | The University of Leeds                               |       1 |
| M        | Exhibition                       | Communication, Cultural and Media Studies, Library and Information Management |           34 | D            | Bath Spa University                                   |       1 |
| M        | Exhibition                       | Communication, Cultural and Media Studies, Library and Information Management |           34 | D            | Bournemouth University                                |       1 |
| M        | Exhibition                       | History                                                                       |           28 | D            | Bath Spa University                                   |       1 |
| M        | Exhibition                       | Music, Drama, Dance, Performing Arts, Film and Screen Studies                 |           33 | D            | Guildhall School of Music & Drama                     |       1 |
| Q        | Digital or visual media          | Art and Design: History, Practice and Theory                                  |           32 | D            | Edinburgh Napier University                           |       7 |
| Q        | Digital or visual media          | Art and Design: History, Practice and Theory                                  |           32 | D            | The University of Cumbria                             |       1 |
| Q        | Digital or visual media          | Communication, Cultural and Media Studies, Library and Information Management |           34 | D            | Bath Spa University                                   |       8 |
| Q        | Digital or visual media          | Communication, Cultural and Media Studies, Library and Information Management |           34 | D            | Bournemouth University                                |       5 |
| Q        | Digital or visual media          | English Language and Literature                                               |           27 | D            | University of Cambridge                               |       1 |
| Q        | Digital or visual media          | Music, Drama, Dance, Performing Arts, Film and Screen Studies                 |           33 | D            | Bath Spa University                                   |       2 |
| S        | Research data sets and databases | Modern Languages and Linguistics                                              |           26 | D            | University of Cambridge                               |       1 |
| T        | Other                            | Anthropology and Development Studies                                          |           22 | C            | School of Oriental and African Studies                |       2 |
| T        | Other                            | Art and Design: History, Practice and Theory                                  |           32 | D            | Abertay University                                    |       9 |
| T        | Other                            | Art and Design: History, Practice and Theory                                  |           32 | D            | Bath Spa University                                   |       8 |
| T        | Other                            | Art and Design: History, Practice and Theory                                  |           32 | D            | Birkbeck College                                      |       7 |
| T        | Other                            | Art and Design: History, Practice and Theory                                  |           32 | D            | De Montfort University                                |       6 |
| T        | Other                            | Art and Design: History, Practice and Theory                                  |           32 | D            | Edinburgh Napier University                           |       3 |
| T        | Other                            | Art and Design: History, Practice and Theory                                  |           32 | D            | Glasgow School of Art                                 |      17 |
| T        | Other                            | Art and Design: History, Practice and Theory                                  |           32 | D            | Liverpool John Moores University                      |      15 |
| T        | Other                            | Art and Design: History, Practice and Theory                                  |           32 | D            | Ravensbourne University London                        |       2 |
| T        | Other                            | Art and Design: History, Practice and Theory                                  |           32 | D            | Royal College of Art(The)                             |      68 |
| T        | Other                            | Art and Design: History, Practice and Theory                                  |           32 | D            | Staffordshire University                              |       1 |
| T        | Other                            | Art and Design: History, Practice and Theory                                  |           32 | D            | The University of Huddersfield                        |      22 |
| T        | Other                            | Art and Design: History, Practice and Theory                                  |           32 | D            | The University of Westminster                         |      18 |
| T        | Other                            | Art and Design: History, Practice and Theory                                  |           32 | D            | University for the Creative Arts                      |      24 |
| T        | Other                            | Art and Design: History, Practice and Theory                                  |           32 | D            | University of Central Lancashire                      |       5 |
| T        | Other                            | Art and Design: History, Practice and Theory                                  |           32 | D            | University of Chester                                 |       4 |
| T        | Other                            | Art and Design: History, Practice and Theory                                  |           32 | D            | University of Derby                                   |      23 |
| T        | Other                            | Art and Design: History, Practice and Theory                                  |           32 | D            | University of Greenwich                               |      15 |
| T        | Other                            | Art and Design: History, Practice and Theory                                  |           32 | D            | University of Portsmouth                              |      14 |
| T        | Other                            | Art and Design: History, Practice and Theory                                  |           32 | D            | University of Southampton                             |       2 |
| T        | Other                            | Communication, Cultural and Media Studies, Library and Information Management |           34 | D            | Bath Spa University                                   |       2 |
| T        | Other                            | Communication, Cultural and Media Studies, Library and Information Management |           34 | D            | Queen Margaret University, Edinburgh                  |       1 |
| T        | Other                            | Communication, Cultural and Media Studies, Library and Information Management |           34 | D            | Staffordshire University                              |       5 |
| T        | Other                            | Communication, Cultural and Media Studies, Library and Information Management |           34 | D            | The University of West London                         |       1 |
| T        | Other                            | Communication, Cultural and Media Studies, Library and Information Management |           34 | D            | University of Glasgow                                 |       5 |
| T        | Other                            | Communication, Cultural and Media Studies, Library and Information Management |           34 | D            | University of Gloucestershire                         |       1 |
| T        | Other                            | Communication, Cultural and Media Studies, Library and Information Management |           34 | D            | University of Winchester                              |       1 |
| T        | Other                            | Communication, Cultural and Media Studies, Library and Information Management |           34 | D            | University of the West of England, Bristol            |       1 |
| T        | Other                            | English Language and Literature                                               |           27 | D            | Bath Spa University                                   |       4 |
| T        | Other                            | English Language and Literature                                               |           27 | D            | Birkbeck College                                      |       1 |
| T        | Other                            | English Language and Literature                                               |           27 | D            | The University of Leeds                               |       1 |
| T        | Other                            | English Language and Literature                                               |           27 | D            | University of Cambridge                               |       1 |
| T        | Other                            | English Language and Literature                                               |           27 | D            | University of Gloucestershire                         |       2 |
| T        | Other                            | Geography and Environmental Studies                                           |           14 | C            | Bath Spa University                                   |       1 |
| T        | Other                            | Music, Drama, Dance, Performing Arts, Film and Screen Studies                 |           33 | D            | Bath Spa University                                   |       5 |
| T        | Other                            | Music, Drama, Dance, Performing Arts, Film and Screen Studies                 |           33 | D            | City, University of London                            |       1 |
| T        | Other                            | Music, Drama, Dance, Performing Arts, Film and Screen Studies                 |           33 | D            | De Montfort University                                |       6 |
| T        | Other                            | Music, Drama, Dance, Performing Arts, Film and Screen Studies                 |           33 | D            | Guildhall School of Music & Drama                     |       1 |
| T        | Other                            | Music, Drama, Dance, Performing Arts, Film and Screen Studies                 |           33 | D            | Leeds Beckett University                              |       3 |
| T        | Other                            | Music, Drama, Dance, Performing Arts, Film and Screen Studies                 |           33 | D            | Queen's University of Belfast                         |       9 |
| T        | Other                            | Music, Drama, Dance, Performing Arts, Film and Screen Studies                 |           33 | D            | The University of Huddersfield                        |      31 |
| T        | Other                            | Music, Drama, Dance, Performing Arts, Film and Screen Studies                 |           33 | D            | The University of West London                         |       1 |
| T        | Other                            | Music, Drama, Dance, Performing Arts, Film and Screen Studies                 |           33 | D            | University of Cambridge                               |       1 |
| T        | Other                            | Music, Drama, Dance, Performing Arts, Film and Screen Studies                 |           33 | D            | University of Glasgow                                 |       1 |
| T        | Other                            | Music, Drama, Dance, Performing Arts, Film and Screen Studies                 |           33 | D            | University of Portsmouth                              |       3 |
| T        | Other                            | Music, Drama, Dance, Performing Arts, Film and Screen Studies                 |           33 | D            | University of South Wales / Prifysgol De Cymru        |       2 |
| T        | Other                            | Music, Drama, Dance, Performing Arts, Film and Screen Studies                 |           33 | D            | University of Southampton                             |       1 |
| T        | Other                            | Music, Drama, Dance, Performing Arts, Film and Screen Studies                 |           33 | D            | University of Winchester                              |       8 |

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


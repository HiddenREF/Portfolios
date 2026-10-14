# Identifying portfolios submitted to REF2021

## Which outputs are portfolios?

This repository explores how portfolio-style submissions can be identified in the published REF2021 output metadata.

The approach is based on the terminology used in the REF2021 guidance. See the REF2021 [Panel criteria and working methods](https://2021.ref.ac.uk/media/1450/ref-2019_02-panel-criteria-and-working-methods.pdf), and [Submitting practice research outputs to REF2021](https://2021.ref.ac.uk/media/1238/submitting-practice-research-outputs-to-ref2021.pdf).

In particular, the terms:

- **`Multi-component`**
- **`contextual information`**

appear to provide the most useful indicators of an output that could have been previously identified as a portfolio.

The script searches REF output metadata for these indicators, including their occurrence in fields such as **title** and **publisher**.

> [!IMPORTANT]
> The outputs identified by this method should be treated as **likely or candidate portfolio outputs**, rather than a definitive list of REF2021 portfolios. "Portfolio" was not a standalone REF output classification, and the method relies on descriptive information available in the published metadata.


## Results

<!-- TABLE_START -->

| output_type   | uoa                                                                           |   unit_of_assessment_number | main_panel   | institution                                           |   count | output_type_name                 |
|:--------------|:------------------------------------------------------------------------------|----------------------------:|:-------------|:------------------------------------------------------|--------:|:---------------------------------|
| I             | English Language and Literature                                               |                          27 | D            | University of Cambridge                               |       1 | Performance                      |
| I             | Music, Drama, Dance, Performing Arts, Film and Screen Studies                 |                          33 | D            | City, University of London                            |       2 | Performance                      |
| I             | Music, Drama, Dance, Performing Arts, Film and Screen Studies                 |                          33 | D            | Guildhall School of Music & Drama                     |       3 | Performance                      |
| J             | Music, Drama, Dance, Performing Arts, Film and Screen Studies                 |                          33 | D            | City, University of London                            |       4 | Composition                      |
| J             | Music, Drama, Dance, Performing Arts, Film and Screen Studies                 |                          33 | D            | Guildhall School of Music & Drama                     |       5 | Composition                      |
| J             | Music, Drama, Dance, Performing Arts, Film and Screen Studies                 |                          33 | D            | The University of West London                         |       1 | Composition                      |
| K             | Art and Design: History, Practice and Theory                                  |                          32 | D            | Anglia Ruskin University Higher Education Corporation |       1 | Design                           |
| L             | Art and Design: History, Practice and Theory                                  |                          32 | D            | Bournemouth University                                |       1 | Artefact                         |
| L             | Art and Design: History, Practice and Theory                                  |                          32 | D            | University of Chester                                 |       1 | Artefact                         |
| M             | Music, Drama, Dance, Performing Arts, Film and Screen Studies                 |                          33 | D            | Guildhall School of Music & Drama                     |       1 | Exhibition                       |
| Q             | Art and Design: History, Practice and Theory                                  |                          32 | D            | Edinburgh Napier University                           |       5 | Digital or visual media          |
| Q             | Art and Design: History, Practice and Theory                                  |                          32 | D            | The University of Cumbria                             |       1 | Digital or visual media          |
| Q             | English Language and Literature                                               |                          27 | D            | University of Cambridge                               |       1 | Digital or visual media          |
| S             | Modern Languages and Linguistics                                              |                          26 | D            | University of Cambridge                               |       1 | Research data sets and databases |
| T             | Art and Design: History, Practice and Theory                                  |                          32 | D            | Edinburgh Napier University                           |       3 | Other                            |
| T             | Art and Design: History, Practice and Theory                                  |                          32 | D            | Liverpool John Moores University                      |      15 | Other                            |
| T             | Art and Design: History, Practice and Theory                                  |                          32 | D            | Royal College of Art(The)                             |      68 | Other                            |
| T             | Art and Design: History, Practice and Theory                                  |                          32 | D            | The University of Huddersfield                        |      20 | Other                            |
| T             | Art and Design: History, Practice and Theory                                  |                          32 | D            | University for the Creative Arts                      |       2 | Other                            |
| T             | Art and Design: History, Practice and Theory                                  |                          32 | D            | University of Chester                                 |       1 | Other                            |
| T             | Art and Design: History, Practice and Theory                                  |                          32 | D            | University of Portsmouth                              |       9 | Other                            |
| T             | Communication, Cultural and Media Studies, Library and Information Management |                          34 | D            | Queen Margaret University, Edinburgh                  |       1 | Other                            |
| T             | Music, Drama, Dance, Performing Arts, Film and Screen Studies                 |                          33 | D            | The University of Huddersfield                        |      23 | Other                            |
| T             | Music, Drama, Dance, Performing Arts, Film and Screen Studies                 |                          33 | D            | University of South Wales / Prifysgol De Cymru        |       2 | Other                            |

<!-- TABLE_END -->


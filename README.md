# IDRISI
IDRISI-R is the largest-scale publicly-available Twitter LMR dataset, in both English and Arabic languages. Named after [_Muhammad Al-Idrisi_](https://en.wikipedia.org/wiki/Muhammad_al-Idrisi), who is one of the pioneers and founders of advanced geography. The "R" refers to the **r**ecognition task. IDRISI-R contains 41 disaster events of different types (e.g., floods, earthquakes) that occurred in a wide geographical area of English and Arabic speaking countries across continents. Around 20K and 4.6K human-labeled tweets (gold) are released for English and Arabic, respectively. Additionally, the first set of around 57K and 1.2M automatically-annotated tweets (sliver) are made available for the research community, for English and Arabic, respectively. The annotated LMs are also labeled for location types (e.g., city, streets, etc.) to enable advanced recognition and finer evaluation of LMR models. In the paper, we conducted quantitative and qualitative analyses that demonstrate IDRISI-R to be second to none in enabling research for LMR task. Moreover, benchmarking \idr{} using the available state-of-the-art NER and LMR models under different task and evaluation setups establishes solid baselines and enables direct comparison for future development.

## Data Release
The tweet datasets naturally support two processing uses cases that are the random and time-based scenarios. Also, they disaster domain imposes some constraints to consider while developing the LMR models. While considerin all these factors, we pack IDRISI-R for release to support research and comparison for different experimental use cases as follows:
- IDRISI-<task>_<lang>_gold_random: the data for every event is randomly shuffled without complying to the nature of Twitter stream. We shuffle the dataset before we fed it to the model. This version is suitable for experimental evaluation of LMR models. 
- IDRISI-<task>_<lang>_gold_timebased: the data of every event is chronologically order to simulate real-world scenarios of stream LMR systems. 
- IDRISI-<task>_<lang>_silver: the data for every event is randomly shuffled and automatically-labeled using BERT-based LMR model. 
- IDRISI-<task>_<lang>_gold_transfere: ...
  
  We provide our data in two formats: 
  (1) _JSON format_ containing, tweet id, text, timestamp, user id, information class (inherited from [humAID](https://crisisnlp.qcri.org/humaid_dataset) and [Kawarith](https://github.com/alaa-a-a/kawarith) English and Arabic datasets, respectively), and list of LMs. Each LM contains its span extracted from the tweet text, the start and end offsets, and the location type. This format give developers the choice to experiment with different processing techniques such as using different tokenization methods, exploring different context expansion methods, employing the social network (recrawled by the tweet ids and user ids), etc. 
  (2) \textit{BILOU format} with 5 position tags (Beginning, Inside, Last, Outside, and Unit), containing only the tokenized text using [SpaCy](https://spacy.io/) and [BreakIterator](https://docs.oracle.com/javase/8/docs/api/java/text/BreakIterator.html) tokenizers for English and Arabic datasets, respectively. We provide the data in BILOU format due to its better performance over the commonly adopted _BIO_ scheme. We further release the IDs of the _sliver_ subsets of IDRISI-R_EN and IDRISI-R_AR. We further make the models, example notebooks to train and run them available for the research community, and the datasets parsing and processing scripts.
 
  
## Annotation Interfaces and instructions
The figures below presents Append and WebAnno interfaces for the English and Arabic LMR annotation tasks, respectively. 

  
## Detailed Results
 
  | <td colspan=9> Random <td colspan=9> Time-based |
  |-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
  | <td colspan=3> CRF <td colspan=3> BERT <td colspan=3> GPNE <td colspan=3> CRF <td colspan=3> BERT <td colspan=3> GPNE |
  | Event | P | R | F1 | P | R | F1 | P | R | F1 | P | R | F1 | P | R | F1 | P | R | F1 |
  | <td colspan=19> Type-less LMR  |
  | Ecuador Earthquake| 0.94 | 0.91 | 0.92 | 0.96 | 0.95 | 0.95 | 0.27 | 0.23 | 0.24 | 0.92 | 0.89 | 0.90 | 0.94 | 0.93 | 0.93 | 0.16 | 0.16 | 0.16 |
  | Canada Wildfires | 0.74 | 0.75 | 0.73 | 0.74 | 0.76 | 0.74 | 0.43 | 0.46 | 0.44 | 0.77 | 0.75 | 0.75 | 0.80 | 0.80 | 0.79 | 0.09 | 0.10 | 0.09 |
  | Italy Earthquake | 0.82 | 0.81 | 0.82 | 0.88 | 0.88 | 0.87 | 0.73 | 0.74 | 0.73 | 0.79 | 0.77 | 0.78 | 0.86 | 0.86 | 0.85 | 0.36 | 0.36 | 0.36  |
  | Kaikoura Earthquake    | 0.88 | 0.87 | 0.87 | 0.92 | 0.92 | 0.91 | 0.60 | 0.60 | 0.59 | 0.91 | 0.88 | 0.88 | 0.91 | 0.89 | 0.89 | 0.17 | 0.17 | 0.17  |
  | Hurricane Matthew      | 0.94 | 0.89 | 0.90 | 0.96 | 0.94 | 0.94 | 0.15 | 0.14 | 0.14 | 0.96 | 0.92 | 0.93 | 0.94 | 0.96 | 0.94 | 0.04 | 0.04 | 0.04  |
  | Sri Lanka Floods       | 0.90 | 0.85 | 0.87 | 0.90 | 0.90 | 0.89 | 0.43 | 0.45 | 0.42 | 0.92 | 0.88 | 0.89 | 0.94 | 0.94 | 0.94 | 0.20 | 0.26 | 0.21  |
  | Hurricane Harvey       | 0.90 | 0.88 | 0.89 | 0.91 | 0.90 | 0.90 | 0.36 | 0.47 | 0.40 | 0.87 | 0.86 | 0.87 | 0.89 | 0.89 | 0.89 | 0.11 | 0.11 | 0.11  |
  | Hurricane Irma         | 0.79 | 0.78 | 0.78 | 0.85 | 0.85 | 0.84 | 0.34 | 0.45 | 0.37 | 0.80 | 0.79 | 0.79 | 0.83 | 0.83 | 0.82 | 0.11 | 0.11 | 0.11  |
  | Hurricane Maria        | 0.91 | 0.88 | 0.88 | 0.92 | 0.91 | 0.91 | 0.45 | 0.56 | 0.48 | 0.89 | 0.85 | 0.86 | 0.92 | 0.94 | 0.92 | 0.19 | 0.22 | 0.19  |
  | Mexico Earthquake      | 0.93 | 0.91 | 0.92 | 0.93 | 0.93 | 0.93 | 0.79 | 0.80 | 0.78 | 0.91 | 0.87 | 0.88 | 0.93 | 0.92 | 0.92 | 0.35 | 0.34 | 0.34  |
  | Maryland Floods        | 0.93 | 0.89 | 0.90 | 0.92 | 0.90 | 0.90 | 0.74 | 0.80 | 0.75 | 0.94 | 0.79 | 0.83 | 0.87 | 0.81 | 0.82 | 0.45 | 0.47 | 0.43  |
  | Greece Wildfires       | 0.95 | 0.93 | 0.93 | 0.93 | 0.93 | 0.92 | 0.83 | 0.80 | 0.79 | 0.91 | 0.88 | 0.88 | 0.90 | 0.89 | 0.88 | 0.45 | 0.39 | 0.39  |
  | Kerala Floods          | 0.87 | 0.83 | 0.84 | 0.89 | 0.90 | 0.88 | 0.69 | 0.69 | 0.66 | 0.93 | 0.88 | 0.89 | 0.93 | 0.93 | 0.92 | 0.29 | 0.30 | 0.27  |
  | Hurricane Florence     | 0.77 | 0.73 | 0.74 | 0.80 | 0.78 | 0.78 | 0.43 | 0.55 | 0.47 | 0.77 | 0.75 | 0.75 | 0.81 | 0.80 | 0.79 | 0.13 | 0.14 | 0.13  |
  | California Wildfires   | 0.91 | 0.89 | 0.89 | 0.92 | 0.93 | 0.92 | 0.72 | 0.77 | 0.73 | 0.92 | 0.89 | 0.90 | 0.90 | 0.90 | 0.89 | 0.30 | 0.33 | 0.30  |
  | Cyclone Idai           | 0.93 | 0.88 | 0.89 | 0.94 | 0.92 | 0.92 | 0.26 | 0.23 | 0.24 | 0.91 | 0.87 | 0.88 | 0.91 | 0.90 | 0.90 | 0.17 | 0.17 | 0.17  |
  | Midwestern U.S. Floods | 0.96 | 0.91 | 0.92 | 0.94 | 0.95 | 0.94 | 0.66 | 0.76 | 0.68 | 0.97 | 0.91 | 0.92 | 0.95 | 0.97 | 0.95 | 0.44 | 0.54 | 0.44  |
  | Hurricane Dorian       | 0.86 | 0.85 | 0.85 | 0.87 | 0.89 | 0.87 | 0.58 | 0.62 | 0.59 | 0.80 | 0.77 | 0.77 | 0.88 | 0.88 | 0.87 | 0.14 | 0.14 | 0.14  |
  | Pakistan Earthquake    | 0.90 | 0.89 | 0.88 | 0.89 | 0.91 | 0.89 | 0.50 | 0.34 | 0.38 | 0.87 | 0.87 | 0.85 | 0.86 | 0.90 | 0.87 | 0.11 | 0.08 | 0.09  |

## Acknowledgments
This work was made possible by the Graduate Sponsorship Research Award (GSRA) #GSRA5-1-0527-18082 from the Qatar National Research Fund (a member of Qatar Foundation). The statements made herein are solely the responsibility of the authors.

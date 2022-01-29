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


| One    | Two | Three | Four    | Five  | Six
|-|-|-|-|-|-
| Span <td colspan=3>triple  <td colspan=2>double
  
## Acknowledgments
This work was made possible by the Graduate Sponsorship Research Award (GSRA) #GSRA5-1-0527-18082 from the Qatar National Research Fund (a member of Qatar Foundation). The statements made herein are solely the responsibility of the authors.

# IDRISI
IDRISI-R is the largest-scale publicly-available Twitter LMR dataset, in both English and Arabic languages. Named after [_Muhammad Al-Idrisi_](https://en.wikipedia.org/wiki/Muhammad_al-Idrisi), who is one of the pioneers and founders of advanced geography. The "R" refers to the _**r**_ecognition task.

It contains 41 disaster events of different types (e.g., floods, earthquakes) that occurred in a wide geographical area of English and Arabic speaking countries across continents. Around 20K and 4.6K human-labeled tweets (gold) are released for English and Arabic, respectively. Additionally, the first set of around 57K and 1.2M automatically-annotated tweets (sliver) are made available for the research community, for English and Arabic, respectively. The annotated LMs are also labeled for location types (e.g., city, streets, etc.) to enable advanced recognition and finer evaluation of LMR models. In the paper, we conducted quantitative and qualitative analyses that demonstrate IDRISI-R to be second to none in enabling research for LMR task. Moreover, benchmarking \idr{} using the available state-of-the-art NER and LMR models under different task and evaluation setups establishes solid baselines and enables direct comparison for future development.

## Data Release
The tweet datasets naturally support two processing uses cases that are the random and time-based scenarios. Also, they disaster domain imposes some constraints to consider while developing the LMR models. While considerin all these factors, we pack IDRISI-R for release to support research and comparison for different experimental use cases as follows:
- IDRISI-<task>_<lang>_gold_random: the data for every event is randomly shuffled without complying to the nature of Twitter stream. We shuffle the dataset before we fed it to the model. This version is suitable for experimental evaluation of LMR models. 
- IDRISI-<task>_<lang>_gold_timebased: the data of every event is chronologically order to simulate real-world scenarios of stream LMR systems. 
- IDRISI-<task>_<lang>_silver: the data for every event is randomly shuffled and automatically-labeled using BERT-based LMR model. 
- IDRISI-<task>_<lang>_gold_transfere: ...
  
  
## Acknowledgments
This work was made possible by the Graduate Sponsorship Research Award (GSRA) #GSRA5-1-0527-18082 from the Qatar National Research Fund (a member of Qatar Foundation). The statements made herein are solely the responsibility of the authors.

# IDRISI
**IDRISI-D** is the largest to date public English and the first Arabic manually-labeled Twitter Location Mention Disambiguation (LMD) datasets. Named after [_Muhammad Al-Idrisi👳🏻‍♂️_](https://en.wikipedia.org/wiki/Muhammad_al-Idrisi), who is one of the pioneers and founders of the advanced geography. The "D" refers to the **d**isambiguation task. IDRISI-D contains 26 disaster events of different types (e.g., floods, earthquakes, fires, etc.) that occurred in a wide geographical area of the English- and Arabic-speaking countries across continents. 
The datasets are annotated for usefulness of features for disambiguation, including event, hashtags, URLs, replies, entities, and other LMs.

IDRISI-D datasets inherit the geographical, domain, location types, temporal, informativeness, and dialectical (for Arabic) coverage from IDRISI-R datasets. 

## Data Release
This dataset is licensed under [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/legalcode).
You can download the IDRISI-D datasets from `data` directory that has the following naming structure: `data/<language>/<event>`

**⚠️ Note**: we are not releasing the _test_ partitions of all datasets since they will be used for evaluation in upcoming challenges and shared tasks. 

We release the datasets in `JSONL` format where every lines corresponds to one tweet with the following properties: 

- `tweet_id`: the tweet id retrieved from the Twitter API. 
- `text`: the text of the tweet.
- `created_at`: the timestamp of the tweet.
- `info_class`: humanitarian categories adopted from [humAID]( https://crisisnlp.qcri.org/humaid_dataset) and [Kwaraith]( https://github.com/alaa-a-a/kawarith) datasets
- `location_mentions`: a list of location mentions (LMs) in the tweet.
	- `text`: the textual span of the LM as it appears in the tweet.
	- `type`: the type of the LM inherited from IDRISI-R datasets.
	- `start_offset`: the start position of the LM in the tweet's text.
	- `end_offset`: the end position of the LM in the tweet's text.
	- `keyword`: keywords used to search OSM during annotation. It's empty when it equals `text`.
	- `osm_url`: the URL to the corresponding toponym assigned by the annotator on OSM.
	- `nominatim_url`: the URL to the corresponding toponym assigned by the annotator on Nominatim.
	- `confidence`: the annotator's confidence score = 1, 2, or 3.
	- `features`: annotator judgements for the usefulness of "event", "hashtags", "urls", "replies", "other_lms", and "entities" features.
	- `osm_json`: the full OSM json object of the corresponding OSM toponym assigned by the annotator.

You may check out an example for JSONL an annotated tweet [here](https://jsoneditoronline.org/#left=cloud.f32a352fa45c4bb2843e490ff3830505).

We processed the data to de-identify it as follows:
- We do not release the the user identifiers, i.e., `user_id`.
- We replace the user mentions (i.e.,`@`) in the tweet text  by `@0` of the same length as the mention length. For example, if the mention is `@someuser`, we replace it with `@00000000`.

We keep the tweet ids, i.e., `id`, to allow recrawling tweets for extracting more information, e.g., meta data, social network properties, etc. This allows developing LMP models that utilize different features beyond the textual content.

  
## Citation
```
  @inproceedings{rsuwaileh2024idrisid,
    title={{IDRISI}-{D}: English and Arabic Location Mention Disambiguation Resources and Tools over Disaster Tweets},
    author={Suwaileh, Reem and Elsayed, Tamer and Imran, Muhammad},
    booktitle = {Proceedings of ArabicNLP 2023},
    month = dec,
    year = {2023},
    address = {Singapore (Hybrid)},
    publisher = {Association for Computational Linguistics},
    url = {https://aclanthology.org/2023.arabicnlp-1.14/},
    doi = {10.18653/v1/2023.arabicnlp-1.14},
    pages = {158--169}
  }
```
  
## Acknowledgments
This work was made possible by the Graduate Sponsorship Research Award (GSRA) #GSRA5-1-0527-18082 from the Qatar National Research Fund (a member of Qatar Foundation). The statements made herein are solely the responsibility of the authors.




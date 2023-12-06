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


%%The \idd{} datasets are released under the Creative Commons Attribution 4.0 International License: \url{https://creativecommons.org/licenses/by/4.0/legalcode}. The location mention and corresponding toponyms in OSM are made available for the community to enable development of effective LMD models. The data is released in \textbf{JSONL} format where every lines corresponds to one post with the following properties: ``text'', ``created\_at'', ``info\_class'' adopted from \hum{} and \kth{} datasets, and ``location\_mentions''. Every LM has the following properties: ``text'', ``type'', ``start\_offset'', ``end\_offset'', ``keyword'' (used to search for the LM on OSM), ``osm\_url'', ``nominatim\_url'', ``confidence'' (the confidence level of the annotator), and ``features'' (list for usefulness annotations).

We processed the data to de-identify it as follows:
\begin{itemize}[noitemsep]
    \item We do not release the user identifiers, i.e., ``user\_id''.
    \item We replace the user mentions (i.e.,``@'') in the post text  by ``@0'' of the same length as the mention length. For example, if the mention is ``@someuser'', we replace it with ``@00000000''.
    %\item We replace the entity mentions (Type PER) in the post text by ``@1'' of the same length as the entity length. For example, if the mention is ``Zakir Naik'', we replace it with ``11111 1111''. We used FARASA NER tool to extract the person entities.
    \item We keep the post ids, i.e., ``id'', to allow recrawling posts for extracting more information, e.g., meta data, social network properties, etc. This allows developing LMR models that utilize different features beyond the textual content.
\end{itemize}

  
## Citation
```
  @inproceedings{rsuwaileh2024idrisid,
    title={IDRISI-D: English and Arabic Location Mention Disambiguation Resources and Tools over Disaster Tweets},
    author={Suwaileh, Reem and Elsayed, Tamer and Imran, Muhammad},
    year={2024},
  }
```
  
## Acknowledgments
This work was made possible by the Graduate Sponsorship Research Award (GSRA) #GSRA5-1-0527-18082 from the Qatar National Research Fund (a member of Qatar Foundation). The statements made herein are solely the responsibility of the authors.

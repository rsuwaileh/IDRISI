# IDRISI
**IDRISI-R** is the largest-scale publicly-available Twitter Location Mention Recognition (LMR) dataset, in both English and Arabic languages. Named after [_Muhammad Al-Idrisi👳🏻‍♂️_](https://en.wikipedia.org/wiki/Muhammad_al-Idrisi), who is one of the pioneers and founders of the advanced geography. The "R" refers to the **r**ecognition task. IDRISI-R contains 41 disaster events of different types (e.g., floods, earthquakes, fires, etc.) that occurred in a wide geographical area of the English- and Arabic-speaking countries across continents. The annotated LMs were also labeled for different coarse- (e.g., country, city) and fine-grained location types (e.g., streets, POIs). The detailed statistics are provided below.


## Data Release
This dataset is licensed under [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/legalcode).
You can download the IDRISI-R datasets from `data` directory that has the following naming structure: `data/<language>/<version>-<setup>-<format>`

**⚠️ Note**: we are not releasing the _test_ partitions of all datasets since they are used for evaluation in the [ITU GeoAI Challange: Location Mention Recognition from Social Media Crisis-related Text](https://geoaichallenge.aiforgood.itu.int/match/matchitem/64). 

**IDRISI-R** is released in two **_versions_**: 
- `gold`: around 20K and 4.6K human-labeled tweets for English and Arabic, respectively. The annotation was collected using crowd and in-house workers for English and Arabic, respectively. 
- `silver`: around 57K and 1.2M automatically annotated English and Arabic tweets, respectively. The annotation was done using the best-performing LMR models.

The tweet datasets naturally support two processing **_setups_** that are:
- `time-based`: tweets are chronologically-ordered.
- `random`: tweets are shuffled randomly while discarding their timestamps.
 
We release the datasets in both `JSONL` and `BILOU` **_formats_**:
- `BILOU`:  NER token-based annotation scheme with 5 classes: Beginning, Inside, Last, Outside, and Unit.
- `JSONL`: every lines corresponds to one tweet with the following properties: `tweet_id`, `user_id`, `text`, `created_at`, `info_class` adopted from [humAID]( https://crisisnlp.qcri.org/humaid_dataset) and [Kwaraith]( https://github.com/alaa-a-a/kawarith) datasets, and `location_mentions`. 

Example:
```
{
  "tweet_id": "1061497252806414336",
  "user_id": "886453870120976384",
  "text": "Please read below!! Another devastating fire has hit Northern California, people need help, whatever you can give, or anyway you can help, please!!",
  "created_at": "Sun Nov 11 05:54:01 +0000 2018",
  "info_class": "requests_or_urgent_needs",
  "location_mentions": [
    {
      "text": "Northern California",
      "type": "STAT",
      "startIdx": 53,
      "endIdx": 72
    }
  ]
}
```

The `gold` version is available for both setups and formats. The `silver` version is available for `random` setup and `JSONL` format only.


| *Event*              | *Date Range*            | *# Twt*|*# Twt<sub>gold</sub>*|*# Twt<sub>LM<sub>0</sub></sub>*| *# LMs (uniq)*  |
|:-|:-|:-|:-|:-|:-|
IDRISI-R<sub>EN</sub>|||||
| Ecuador Earthquake   | 2016/04/17 - 2016/04/18 | 1,594  | 1,153        | 205            | 1,178 (116)   | 
| Canada Wildfires     | 2016/05/06 - 2016/05/27 | 2,259  | 1,300        | 277            | 1,333 (165)   | 
| Italy Earthquake     | 2016/08/24 - 2016/08/29 | 1,240  | 590          | 360            | 284 (66)      | 
| Kaikoura Earthquake  | 2016/09/01 - 2016/11/22 | 2,217  | 1,231        | 375            | 1,133 (227)   | 
| Hurricane Matthew    | 2016/10/04 - 2016/10/10 | 1,659  | 855          | 62             | 1,132 (119)   | 
| Sri Lanka Floods     | 2017/05/31 - 2017/07/03 | 575    | 457          | 88             | 521 (105)     | 
| Hurricane Harvey     | 2017/08/25 - 2017/09/01 | 9,164  | 1,299        | 719            | 753 (182)     | 
| Hurricane Irma       | 2017/09/06 - 2017/09/17 | 9,467  | 1,298        | 563            | 951 (354)     | 
| Hurricane Maria      | 2017/09/16 - 2017/10/02 | 7,328  | 1,299        | 357            | 1,165 (217)   | 
| Mexico Earthquake    | 2017/09/20 - 2017/09/23 | 2,036  | 1,300        | 132            | 1,396 (116)   | 
| Maryland Floods      | 2018/05/28 - 2018/06/07 | 747    | 422          | 28             | 693 (89)      | 
| Greece Wildfires     | 2018/07/24 - 2018/08/18 | 1,526  | 967          | 123            | 1,365 (156)   | 
| Kerala Floods        | 2018/08/17 - 2018/08/31 | 8,056  | 1,300        | 331            | 1,656 (367)   | 
| Hurricane Florence   | 2018/09/11 - 2018/09/18 | 6,359  | 1,300        | 559            | 1,245 (403)   |  
| California Wildfires | 2018/11/10 - 2018/12/07 | 7,444  | 1,300        | 455            | 1,075 (181)   | 
| Cyclone Idai         | 2019/03/15 - 2019/04/16 | 3,944  | 1,300        | 376            | 1,744 (268)   | 
| Midwest. US Floods   | 2019/03/25 - 2019/04/03 | 1,930  | 1,076        | 92             | 1,592 (189)   | 
| Hurricane Dorian     | 2019/08/30 - 2019/09/02 | 7,660  | 1,300        | 492            | 1,260 (325)   | 
| Pakistan Earthquake  | 2019/09/24 - 2019/09/26 | 1,991  | 767          | 129            | 1,403 (185)   | 
| **Total**            |**2016/04/17 - 2019/09/26**|**77,196**| **20,514**     | **5,723**        | **21,879 (3,830)**|
IDRISI-R<sub>AR</sub>	||||||
| Jordan Floods        | 2018/10/25 - 2018/10/27 | 638    | 527          | 63             | 550 (97)       | 
| Kuwait Floods        | 2018/04/11 - 2018/04/14 | 1,665  | 1,269        | 1              | 623 (67)       |
| Cairo Bombing        | 2019/08/04 - 2019/08/04 | 369    | 268          | 777            | 939 (390)      | 
| Hafr Floods          | 2019/10/25 - 2019/10/28 | 658    | 514          | 122            | 338 (192)      | 
| Dragon Storms        | 2020/03/12 - 2020/03/15 | 427    | 305          | 46             | 752 (172)      | 
| Beirut Explosion     | 2020/08/04 - 2020/08/04 | 420    | 349          | 107            | 897 (177)      | 
| CoVID-19             | 2019/12/01 - 2020/12/30 | 2,005   | 1,361         | 503            | 1,137 (275)    | 
| **Total**            | **2018/10/25 - ongoing**|**6,182**| **4,593**   | **1,619**      | **5,236 (1,370)**| 


We processed the data to de-identify it as follows:
- We do not release the the user identifiers, i.e., `user_id`.
- We replace the user mentions (i.e.,`@`) in the tweet text  by `@0` of the same length as the mention length. For example, if the mention is `@someuser`, we replace it with `@00000000`.

We keep the tweet ids, i.e., `id`, to allow recrawling tweets for extracting more information, e.g., meta data, social network properties, etc. This allows developing LMP models that utilize different features beyond the textual content.
  
## Citation
```
@article{rsuwaileh2023idrisire,
    title = {{IDRISI}-{RE}: A generalizable dataset with benchmarks for location mention recognition on disaster tweets},
    author = {Reem Suwaileh and Tamer Elsayed and Muhammad Imran},
    journal = {Information Processing & Management},
    volume = {60},
    number = {3},
    pages = {103340},
    year = {2023},
    issn = {0306-4573},
    doi = {https://doi.org/10.1016/j.ipm.2023.103340},
    url = {https://www.sciencedirect.com/science/article/pii/S0306457323000778},
    publisher={Elsevier}
  }

  
  @inprocessdings{rsuwaileh2023idrisira,
    title = {{IDRISI}-{RA}: The First {A}rabic Location Mention Recognition Dataset of Disaster Tweets},
    author = {Suwaileh, Reem  and Imran, Muhammad and Elsayed, Tamer},
    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
    month = jul,
    year = {2023},
    address = {Toronto, Canada},
    publisher = {Association for Computational Linguistics},
    url = {https://aclanthology.org/2023.acl-long.901},
    doi = {10.18653/v1/2023.acl-long.901},
    pages = {16298--16317}
  }
```
  
## Acknowledgments
This work was made possible by the Graduate Sponsorship Research Award (GSRA) #GSRA5-1-0527-18082 from the Qatar National Research Fund (a member of Qatar Foundation). The statements made herein are solely the responsibility of the authors.

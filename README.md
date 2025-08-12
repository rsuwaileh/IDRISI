# IDRISI
**IDRISI** is the largest-scale publicly-available Twitter Location Mention Prediction (LMP) dataset, in both English and Arabic languages. Named after [_Muhammad Al-Idrisi👳🏻‍♂️_](https://en.wikipedia.org/wiki/Muhammad_al-Idrisi), who is one of the pioneers and founders of the advanced geography. 

All datasets are licensed under [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/legalcode).

- The Location Mention Recognition (LMR) datasets are under [LMR](https://github.com/rsuwaileh/IDRISI/tree/main/LMR) directory.
- The Location Mention Disambiguation (LMD) datasets will be available soon under [LMD](https://github.com/rsuwaileh/IDRISI/tree/main/LMD) directory.



We processed the data to de-identify it as follows:
- We do not release the the user identifiers, i.e., `user_id`.
- We replace the user mentions (i.e.,`@`) in the tweet text  by `@0` of the same length as the mention length. For example, if the mention is `@someuser`, we replace it with `@00000000`.

We keep the tweet ids, i.e., `id`, to allow recrawling tweets for extracting more information, e.g., meta data, social network properties, etc. This allows developing LMP models that utilize different features beyond the textual content.

For any inqueries, please create a new issue in the repository or contact us via email:
- Reem Suwaileh: `rs081123@qu.edu.qa`

  
## Publications
```
  @article{rsuwaileh2023idrisire,
    title = {{IDRISI-RE}: A generalizable dataset with benchmarks for location mention recognition on disaster tweets},
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


  @inproceedings{rsuwaileh2024idrisid,
    title={{IDRISI-D}: English and Arabic Location Mention Disambiguation Resources and Tools over Disaster Tweets},
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

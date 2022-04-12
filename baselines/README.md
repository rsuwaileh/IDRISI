## LMR models 
To establishe solid baselines and enables direct comparison for future development, we benchmarked IDRISI using the available state-of-the-art NER and LMR models under different task and evaluation setups. More details on the models and setups exist in the article (to be made available soon).

**English models**:
- CRF: we adopted the Conditional Random Fields models from the [crfsuite library](https://sklearn-crfsuite.readthedocs.io/). To run this model, run the examples in `en-crf` notebook. 
- BERT: we adopted the NER example of [HuggingFace](https://huggingface.co/) library. To run this model, follow the steps in [this forked version](https://github.com/rsuwaileh/transformers/tree/master/examples/ner).
- GazPNE: we run a free annotations LMR model that achieved the SOTA results. We note that GazPNE achieved SOTA results under different evaluation assumptions than ours such as (1) focusing on detecting location within the affected area, and (2) using different flood-focused datasets for testing. To run this model, check the guidelines in [its original repository](https://github.com/uhuohuy/GazPNE).

**Arabic models**:
- CML: we used the CAMeLBERT-Mix NER model that is trained on the ANERcorp dataset. ANERcorp contains Moden Standard Arabic (MSA), Dialectal Arabic (DA), and Classical Arabic (CA) data. To run the model, follow the steps here(https://huggingface.co/CAMeL-Lab/bert-base-arabic-camelbert-mix-ner). To run this model, run the examples in `ar-ner` notebook.
- FRSA: we used the commonly used NER model called Farasa through it [REST API](https://farasa.qcri.org/NER/). To run this model, run the examples in `ar-ner` notebook.
- CRF: similar to English, we trained a CRF model due to its competetive performance. To run this model, run the examples in `ar-crf` notebook.
- BERT: similar to English, we trained a BERT-based LMR modelusing the MARBERT Arabic model. To run this model, run the examples in `ar-bert` notebook.


## Detailed Results
Below are the detailed results using Precision, Recall, and F1 measures. We use different evaluation setups that we elaborate on in the article (to be made available soon).

### English Results

  ||Random |||||||||Time-based|||||||||
  |-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
  ||CRF |||BERT|||GPNE|||CRF|||BERT |||GPNE|||
  | Event | P | R | F1 | P | R | F1 | P | R | F1 | P | R | F1 | P | R | F1 | P | R | F1 |
  | Type-less LMR |||||||||||||||||||
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
| Type-based LMR |||||||||||||||||||
| Ecuador Earthquake     | 0.98 | 0.98 | 0.98 | 0.98 | 0.98 | 0.98 |  -   |  -   |  -   | 0.98 | 0.97 | 0.97 | 0.97 | 0.97 | 0.97 |  -   |  -   |   -   |
| Canada Wildfires       | 0.94 | 0.94 | 0.94 | 0.93 | 0.93 | 0.93 |  -   |  -   |  -   | 0.94 | 0.94 | 0.94 | 0.94 | 0.94 | 0.94 |  -   |  -   |   -   |
| Italy Earthquake       | 0.98 | 0.98 | 0.98 | 0.98 | 0.98 | 0.98 |  -   |  -   |  -   | 0.96 | 0.96 | 0.96 | 0.95 | 0.95 | 0.95 |  -   |  -   |   -   |
| Kaikoura Earthquake    | 0.98 | 0.98 | 0.98 | 0.98 | 0.98 | 0.98 |  -   |  -   |  -   | 0.98 | 0.98 | 0.98 | 0.98 | 0.98 | 0.98 |  -   |  -   |   -   |
| Hurricane Matthew      | 0.97 | 0.97 | 0.97 | 0.97 | 0.97 | 0.97 |  -   |  -   |  -   | 0.97 | 0.96 | 0.96 | 0.96 | 0.97 | 0.96 |  -   |  -   |   -   |
| Sri Lanka Floods       | 0.95 | 0.94 | 0.94 | 0.93 | 0.93 | 0.93 |  -   |  -   |  -   | 0.97 | 0.97 | 0.97 | 0.94 | 0.95 | 0.94 |  -   |  -   |   -   |
| Hurricane Harvey       | 0.97 | 0.97 | 0.97 | 0.98 | 0.98 | 0.98 |  -   |  -   |  -   | 0.98 | 0.97 | 0.97 | 0.98 | 0.98 | 0.98 |  -   |  -   |   -   |
| Hurricane Irma         | 0.97 | 0.97 | 0.97 | 0.96 | 0.96 | 0.96 |  -   |  -   |  -   | 0.96 | 0.96 | 0.96 | 0.97 | 0.97 | 0.97 |  -   |  -   |   -   |
| Hurricane Maria        | 0.97 | 0.97 | 0.97 | 0.97 | 0.97 | 0.97 |  -   |  -   |  -   | 0.97 | 0.97 | 0.97 | 0.97 | 0.97 | 0.97 |  -   |  -   |   -   |
| Mexico Earthquake      | 0.97 | 0.96 | 0.96 | 0.97 | 0.97 | 0.97 |  -   |  -   |  -   | 0.96 | 0.96 | 0.96 | 0.96 | 0.96 | 0.96 |  -   |  -   |   -   |
| Maryland Floods        | 0.94 | 0.94 | 0.94 | 0.93 | 0.94 | 0.93 |  -   |  -   |  -   | 0.96 | 0.95 | 0.95 | 0.96 | 0.95 | 0.95 |  -   |  -   |   -   |
| Greece Wildfires       | 0.97 | 0.97 | 0.97 | 0.97 | 0.97 | 0.97 |  -   |  -   |  -   | 0.95 | 0.95 | 0.95 | 0.95 | 0.95 | 0.95 |  -   |  -   |   -   |
| Kerala Floods          | 0.96 | 0.96 | 0.96 | 0.96 | 0.96 | 0.96 |  -   |  -   |  -   | 0.96 | 0.96 | 0.96 | 0.97 | 0.97 | 0.96 |  -   |  -   |   -   |
| Hurricane Florence     | 0.96 | 0.96 | 0.96 | 0.96 | 0.96 | 0.96 |  -   |  -   |  -   | 0.96 | 0.96 | 0.96 | 0.96 | 0.97 | 0.96 |  -   |  -   |   -   |
| California Wildfires   | 0.98 | 0.98 | 0.98 | 0.98 | 0.98 | 0.98 |  -   |  -   |  -   | 0.98 | 0.98 | 0.98 | 0.98 | 0.98 | 0.98 |  -   |  -   |   -   |
| Cyclone Idai           | 0.98 | 0.97 | 0.97 | 0.97 | 0.97 | 0.97 |  -   |  -   |  -   | 0.98 | 0.97 | 0.97 | 0.97 | 0.98 | 0.97 |  -   |  -   |   -   |
| Midwestern U.S. Floods | 0.98 | 0.97 | 0.97 | 0.98 | 0.98 | 0.98 |  -   |  -   |  -   | 0.98 | 0.98 | 0.98 | 0.98 | 0.98 | 0.98 |  -   |  -   |   -   |
| Hurricane Dorian       | 0.96 | 0.96 | 0.96 | 0.96 | 0.97 | 0.97 |  -   |  -   |  -   | 0.96 | 0.95 | 0.95 | 0.97 | 0.97 | 0.97 |  -   |  -   |   -   |
| Pakistan Earthquake    | 0.94 | 0.94 | 0.94 | 0.95 | 0.95 | 0.95 |  -   |  -   |  -   | 0.93 | 0.93 | 0.93 | 0.94 | 0.94 | 0.93 |  -   |  -   |   -   |



### Arabic Results

||Random ||||||||||||Time-based||||||||||||
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
||CRF |||BERT|||CML|||FRSA|||CRF |||BERT|||CML|||FRSA|||
| Event | P | R | F1 | P | R | F1 | P | R | F1 | P | R | F1 | P | R | F1 | P | R | F1 | P | R | F1 | P | R | F1 |
| Type-less LMR |||||||||||||||||||||||||
| Jordan Floods | 0.54 | 0.54 | 0.54 | 0.92 | 0.94 | 0.93 | 0.46 | 0.64 | 0.52 | 0.65 | 0.65 | 0.65 | 0.56 | 0.57 | 0.56 | 0.86 | 0.91 | 0.88 | 0.41 | 0.67 | 0.49 | 0.64 | 0.64 | 0.64  |
| Kuwait Floods | 0.61 | 0.61 | 0.61 | 0.97 | 0.97 | 0.97 | 0.26 | 0.47 | 0.32 | 0.69 | 0.69 | 0.69  | 0.53 | 0.52 | 0.53 | 0.93 | 0.93 | 0.93 | 0.24 | 0.43 | 0.29 | 0.62 | 0.62 | 0.62  |
| Cairo Bombing | 0.44 | 0.41 | 0.40 | 0.95 | 0.96 | 0.95 | 0.38 | 0.18 | 0.24 | 0.06 | 0.06 | 0.06 | 0.59 | 0.60 | 0.56 | 0.95 | 0.96 | 0.95 | 0.35 | 0.21 | 0.25 | 0.09 | 0.08 | 0.08  |
| Hafr Floods | 0.27 | 0.28 | 0.27 | 0.85 | 0.85 | 0.85 | 0.31 | 0.33 | 0.30 | 0.29 | 0.29 | 0.29 | 0.41 | 0.41 | 0.40 | 0.84 | 0.85 | 0.84 | 0.33 | 0.34 | 0.32 | 0.28 | 0.28 | 0.28  |
| Dragon Storms | 0.63 | 0.63 | 0.63 | 0.85 | 0.87 | 0.86 | 0.56 | 0.63 | 0.58 | 0.74 | 0.74 | 0.74 | 0.67 | 0.67 | 0.67 | 0.79 | 0.81 | 0.80 | 0.62 | 0.64 | 0.61 | 0.70 | 0.70 | 0.70  |
| Beirut Explosion | 0.51 | 0.51 | 0.51 | 0.59 | 0.59 | 0.59 | 0.51 | 0.64 | 0.54 | 0.49 | 0.49 | 0.49 | 0.62 | 0.62 | 0.62 | 0.43 | 0.47 | 0.44 | 0.45 | 0.70 | 0.52 | 0.71 | 0.71 | 0.71  |
| CoVID-19 | 0.87 | 0.87 | 0.87 | 0.94 | 0.94 | 0.94 | 0.19 | 0.34 | 0.24 | 0.85 | 0.85 | 0.85 | 0.84 | 0.84 | 0.84 | 0.93 | 0.92 | 0.92 | 0.22 | 0.39 | 0.27 | 0.80 | 0.80 | 0.80  |
| Type-based LMR |||||||||||||||||||||||||
| Jordan Floods | 0.57 | 0.57 | 0.57 | 0.83 | 0.83 | 0.83 | - | - | - | - | - | - | 0.60 | 0.60 | 0.60 | 0.80 | 0.81 | 0.80 | - | - | - | - | - | -  |
| Kuwait Floods | 0.63 | 0.63 | 0.63 | 0.94 | 0.94 | 0.94 | - | - | - | - | - | - | 0.54 | 0.54 | 0.54 | 0.89 | 0.88 | 0.88 | - | - | - | - | - | -  |
| Cairo Bombing | 0.46 | 0.41 | 0.41 | 0.93 | 0.93 | 0.93 | - | - | - | - | - | - | 0.59 | 0.60 | 0.56 | 0.91 | 0.94 | 0.92 | - | - | - | - | - | -  |
| Hafr Floods | 0.28 | 0.29 | 0.28 | 0.75 | 0.76 | 0.75 | - | - | - | - | - | - | 0.44 | 0.43 | 0.43 | 0.82 | 0.83 | 0.82 | - | - | - | - | - | -  |
| Dragon Storms | 0.70 | 0.70 | 0.70 | 0.75 | 0.75 | 0.75 | - | - | - | - | - | - | 0.70 | 0.70 | 0.70 | 0.74 | 0.74 | 0.74 | - | - | - | - | - | -  |
| Beirut Explosion | 0.51 | 0.51 | 0.51 | 0.59 | 0.59 | 0.59 | - | - | - | - | - | - | 0.68 | 0.68 | 0.68 | 0.78 | 0.78 | 0.78 | - | - | - | - | - | -  |
| CoVID-19 | 0.89 | 0.89 | 0.89 | 0.91 | 0.91 | 0.91 | - | - | - | - | - | - | 0.85 | 0.85 | 0.85 | 0.86 | 0.86 | 0.86 | - | - | - | - | - | -  |



The F1 results of CAMeLBERT models on IDRISI-R__AR_. The best score is boldfaced per dataset per experimental scenario.


|| Random |||| Time-based||||
|-|-|-|-|-|-|-|-|-|
| Event | CA | MSA | DA | MIX | CA | MSA | DA | MIX |
| Jordan Floods | 0.378 | **0.543** | 0.326 | 0.517 | 0.377 | **0.499** | 0.340 | 0.491 |
| Kuwait Floods | 0.288 | 0.314 | 0.277 | **0.320** | 0.250 | 0.286 | 0.261 | **0.294** |
| Cairo Bombing | 0.082 | **0.316** | 0.080 | 0.237 | 0.089 | 0.302 | 0.108 | **0.250** |
| Hafr Floods | 0.121 | 0.302 | **0.498** | 0.303 | 0.093 | 0.315 | **0.595** | 0.319 |
| Dragon Storms | 0.565 | 0.539 | 0.445 | **0.579** | 0.595 | 0.573 | 0.571 | **0.615** |
| Beirut Explosion | 0.504 | 0.531 | 0.485 | **0.539** | **0.520** | 0.517 | 0.464 | **0.520** |
| CoVID-19 | **0.347** | 0.248 | 0.312 | 0.238 | **0.351** | 0.261 | 0.342 | 0.266 |




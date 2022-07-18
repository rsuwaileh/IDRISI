The results reported under `IDRISI/baselines` are for the BERT-based LMR models that are trained and finetuned per disaster event from IDRISI-R dataset. As it is not practical to release 19 English and 6 Arabic models for every disaster event, we release four models per language that are trained using the training splits of all events from IDRISI-R dataset under different data and task setups. The underlying BERT-based model is adopted from the [TLLMR4CM GitHub](https://github.com/rsuwaileh/TLLMR4CM/). 

The data setups are:
  - `Random`:  The timestamps of tweets are ignored during training.
  - `Time-based`:  The tweets are chronologically-ordered during training.
  
The task setups are: 
  - `Type-based`: The LMR model is trained to identify the toponyms' spans in the text and predict their location types. The location type can be coarse-grained (e.g., country, city, etc.) and fine-grained (e.g., street, POI, etc.)
  - `Type-less`: The LMR model is trained to identify the toponyms' spans in the text without predicting their location types.


We tuned each model in light of the recommended hyperparameters and values [in BERT paper](https://aclanthology.org/N19-1423.pdf): batch size of 8, 16 or 32, number of epochs of 2, 3, or 4, and learning rate of 5E-5, 3E-5, or 2E-5. We only release the best performing models on the development splits of IDRISI-R dataset and report the best hyperparameters values.

The models are available through HuggingFace:

| Target Event | `#epochs` | `#training_batches` | `learning_rate` | 
|:-|:-|:-|:-|
| [IDRISI-LMR-EN-random-typebased](https://huggingface.co/rsuwaileh/IDRISI-LMR-EN-random-typebased/) | 2 | 32 | 4E-5 |
| [IDRISI-LMR-EN-random-typeless](https://huggingface.co/rsuwaileh/IDRISI-LMR-EN-random-typeless/) | 2 | 16 | 4E-5 | 
| [IDRISI-LMR-EN-timebased-typebased](https://huggingface.co/rsuwaileh/IDRISI-LMR-EN-timebased-typebased/) | 3 | 8 | 4E-5 |
| [IDRISI-LMR-EN-timebased-typeless](https://huggingface.co/rsuwaileh/IDRISI-LMR-EN-timebased-typeless/) | 2 | 8 | 5E-5 |
| [IDRISI-LMR-AR-random-typebased](https://huggingface.co/rsuwaileh/IDRISI-LMR-AR-random-typebased/) | 2 | 32 | 4E-5 |
| [IDRISI-LMR-AR-random-typeless](https://huggingface.co/rsuwaileh/IDRISI-LMR-AR-random-typeless/) | 2 | 16 | 4E-5 | 
| [IDRISI-LMR-AR-timebased-typebased](https://huggingface.co/rsuwaileh/IDRISI-LMR-AR-timebased-typebased/) | 3 | 8 | 4E-5 |
| [IDRISI-LMR-AR-timebased-typeless](https://huggingface.co/rsuwaileh/IDRISI-LMR-AR-timebased-typeless/) | 2 | 8 | 5E-5 |

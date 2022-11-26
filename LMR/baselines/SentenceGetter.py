'''
Created on Oct 22, 2019

@author: Reem
'''
# Since we will treat the NER process as a multi-class classification, 
# we need to make the training data into “token-label” form, 
# we need to parse the sentence from data set:

class SentenceGetter(object):
    
    def __init__(self, data):
        self.n_sent = 1
        self.data = data
        self.empty = False
        agg_func = lambda s: [(w, p, t) for w, p, t in zip(s["Word"].values.tolist(),
                                                           s["POS"].values.tolist(),
                                                           s["Tag"].values.tolist())]
        self.grouped = self.data.groupby("Sentence #").apply(agg_func)
        #print('self.grouped')
        #print(len(self.grouped))
        self.sentences = [s for s in self.grouped]
        
    def get_next(self):
        try:
            s = self.data[self.data["Sentence #"] == "Sentence: {}".format(self.n_sent)]
            self.n_sent += 1
            return s["Word"].values.tolist(), s["POS"].values.tolist(), s["Tag"].values.tolist()    
        except:
            self.empty = True
            return None, None, None
    
        def get_next(self):
            try:
                s = self.grouped["Sentence: {}".format(self.n_sent)]
                self.n_sent += 1
                return s
            except:
                return None

    

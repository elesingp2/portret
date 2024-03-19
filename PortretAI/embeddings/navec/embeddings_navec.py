import gensim.downloader as api
from gensim.models import Word2Vec
import pandas as pd
import numpy as np
from navec import Navec


class w2v_vectorizer:
    def __init__(self):
        """
            инициализирует предобученную модель word2vec 
        """
        self.path = '/workspaces/portret/PortretAI/embeddings/navec/navec_news_v1_1B_250K_300d_100q (2).tar'
        self.model = Navec.load(self.path)


    def transform(self,comments,w2v=300):
        '''
            векторизует комментарии
        '''
        print("starting vect")
        i=0
        embed=np.zeros((len(comments),w2v))
        for line in comments:
            vec=np.zeros(w2v)
            j=0
            if line!=None:
                for token in line:      
                    if token in self.model:
                        vec+=self.model[token]
                    else:
                        #print(token)
                        vec+=np.zeros(w2v)
                    j+=1
                embed[i]=vec/j
                                    
            else:
                embed[i]=np.zeros(w2v)
            i+=1
        print("ending vec")
        return embed



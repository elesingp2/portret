import nltk
import re
from pymorphy3 import MorphAnalyzer
from nltk.corpus import stopwords

nltk.download('stopwords')


class preprocess_clusterization:
    def __init__(self):
        self.patterns = "[A-Za-z0-9!#$%&'()*+,./:;<=>?@[\]^_`{|}~—\"\-]+" #patterns to substitute
        self.stopwords_ru = stopwords.words("russian") #russina stopwords
        self.morph = MorphAnalyzer() #for lemmatization

    def remove_emoji(self,line):
        emoji_pattern = re.compile("["
                        u"\U0001F600-\U0001F64F"  # emoticons
                        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                        u"\U0001F680-\U0001F6FF"  # transport & map symbols
                        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                        u"\U00002702-\U000027B0"
                        u"\U000024C2-\U0001F251"
                        u"\U0001f926-\U0001f937"
                        u"\U0001F1F2"
                        u"\U0001F1F4"
                        u"\U0001F620"
                        u"\u200d"
                        u"\u2640-\u2642"
                        u"\u2600-\u2B55"
                        u"\u23cf"
                        u"\u23e9"
                        u"\u231a"
                        u"\ufe0f"  # dingbats
                        u"\u3030"
                        u"\U00002500-\U00002BEF"  # Chinese char
                        u"\U00010000-\U0010ffff"
                        "]+", flags=re.UNICODE)
        
        return emoji_pattern.sub(r'', line)

    def preprocess_text_morph(self,doc,tken=False):
        doc = re.sub(self.patterns, ' ', doc)
        doc=self.remove_emoji(doc)
        if tken:
            tokens = []
            for token in doc.split():
                if token and token not in self.stopwords_ru:
                    token = token.strip()
                    token = self.morph.normal_forms(token)[0]
                    tokens.append(token)
            #print(tokens)
            if len(tokens) >= 2:
                return tokens
                #print(tokens)
            return [""]
        else:
            return doc
import pandas as pd
import numpy as np
import textdistance
import re
from collections import Counter

words = []
with open('/content/drive/MyDrive/Data Science/words.txt', 'r') as f:
    file_name_data = f.read()
    file_name_data=file_name_data.lower()
    words = re.findall('\w+',file_name_data)

All_words = set(words)


word_freq_dict = {}  
word_freq_dict = Counter(words)

    
Total = sum(word_freq_dict.values())    
for k in word_freq_dict.keys():
    probs[k] = word_freq_dict[k]/Total

def spelling_correcter(input_word):
    input_word = input_word.lower()
    if input_word in All_words:
        return('That might actually be a correct spelling')
    else:
        similarities = [1-(textdistance.Jaccard(qval=2).distance(v,input_word)) for v in word_freq_dict.keys()]
        df = pd.DataFrame.from_dict(probs, orient='index').reset_index()
        df = df.rename(columns={'index':'Word'})
        df['Similarity'] = similarities
        most_likey_word = df.sort_values(['Similarity'], ascending=False).head()
        return list(most_likey_word["Word"])[0],list(most_likey_word["Word"])[1],list(most_likey_word["Word"])[2]

print(spelling_correcter("wonderng"))


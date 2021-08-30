#VECTORISATION
#This is important because machine learning algorithms understand data that is in numerical form,so we have to convert text to that form to do machine learning on the data

from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd


vect = CountVectorizer()
text = ["Hi, my name is Inga", "How are you?"]
vect.fit(text)
train = vect.transform(text)
train.toarray()
data = pd.DataFrame(train.toarray(), columns=vect.get_feature_names())
print(data)

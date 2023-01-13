import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
from  sklearn.datasets import fetch_20newsgroups
import pandas as pd 

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import confusion_matrix

data = pd.read_csv("checkpoint.csv")


train = pd.DataFrame()
test = pd.DataFrame()

for subcat in data.Subcategory.unique():
    data_sub = data[data.Subcategory == subcat]
    sindex = int(np.round(len(data_sub)*.8))
    if len(test)==0:
        train  = data_sub[:sindex]
        test = data_sub[sindex:] 
    else:
        train  = train.append(data_sub[:sindex])
        test = test.append(data_sub[sindex:] )

#Convert column to list
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(train.name.values, train.Subcategory.values)
labels = model.predict(test.name.values)


mat = confusion_matrix(test.Subcategory.values, labels)

sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False)
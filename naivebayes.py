%matplotlib inline
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
import sklearn.datasets import fetch_20newgroups

from sklearn.feature_extraction.text import TfidVectorizer
from sklearn.naivebayes import MultinomialNB
from sklearn.pipeline import make_pipeline

from sklearn.metrics import confusion_matrix

 
mat = confusion_matrix(test.taget, labels)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,
            xticklabels =train.target_names,
            yticklabels = train.target_names)

data = fetch_20newgroups()
data.target_names


model = make_pipeline(TfidVectorizer(), MultinomialNB())
model.fit(train.data, train.target)
labels = model.predict(test.data)



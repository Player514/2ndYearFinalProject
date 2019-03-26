# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 21:19:32 2019

@author: bianc
"""

from pandas import DataFrame
import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string
from nltk.stem import WordNetLemmatizer

#Read data as pandas
df=pd.read_csv("phase1_movie_reviews-train.csv")
text=df["reviewText"][0]

tokenized = nltk.word_tokenize(text)

for token in nltk.word_tokenize(text):
    print(token)
    
#Removing stopwords

words = nltk.word_tokenize(text)
for word in words:
    filtered_words = []
    if word not in stopwords:
        filtered_words.append(word)
        
print(filtered_words)

#Stemming:
ps = PorterStemmer()
for w in filtered_words:
    print(ps.stem(w))
    
    
#Lemmatizing:
lem = WordNetLemmatizer()
for w in words:
    print(lem.lemmatize(w))
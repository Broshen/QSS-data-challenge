import os
import json
import string
import csv
# import nltk

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import word_tokenize, wordpunct_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
import numpy as np
from sklearn import metrics
from sklearn.metrics import pairwise_distances
from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.externals import joblib

root_dir = "./"
from textblob import TextBlob
from nltk.corpus import stopwords

parts = [
'parts/aa',
'parts/ab',
'parts/ac',
'parts/ad',
'parts/ae',
'parts/af',
'parts/ag',
'parts/ah',
'parts/ai',
'parts/aj',
'parts/ak',
'parts/al',
'parts/am',
'parts/an',
'parts/ao',
]

test = [
'test/aa',
'test/ab',
'test/ac',
'test/ad',
'test/ae',
'test/af',
]

def writeToCSV(jsonFiles, csvFile):
    with open(csvFile, 'w', newline='', encoding='utf-8') as csvfile:
        # Instantiates a client
        writer = csv.writer(csvfile)
        count=0
        for part in jsonFiles:
            print("writing " + part)
            with open(root_dir + part, encoding='utf-8') as data_file:    
                yelp = json.load(data_file)
                for review in yelp:
                    reviewText = TextBlob(review["text"])
                    review["sentiment_score_1"] = reviewText.sentiment.polarity

                    lista = [word for word in reviewText.words if word not in stopwords.words('english')]
                    reviewText = ' '.join(lista)
                    print(reviewText)
                    reviewText = TextBlob(reviewText)
                    review["sentiment_score_2"] = reviewText.sentiment.polarity
                    if count == 0:
                        header = review.keys()
                        writer.writerow(header)
                        count += 1

                    writer.writerow(review.values())

#writeToCSV(test, "dataToPredict.csv")
#writeToCSV(parts, "data.csv")
writeToCSV(['first12.json'], 'datatest.csv')


import pandas as pd

from sklearn.linear_model import SGDClassifier 
from sklearn.svm import LinearSVC 

from sklearn.feature_extraction.text import HashingVectorizer

from sklearn.model_selection import train_test_split

from sklearn.pipeline import Pipeline

from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import accuracy_score

yelp = pd.read_csv('./datashort.csv')

X = yelp['text']
y = yelp['stars']

#predict = pd.read_csv('./dataToPredict.csv')

# X_test = predict['text']


# bow_transformer = HashingVectorizer(stop_words='english').fit(X)
# print('transforming data')
# X = bow_transformer.transform(X)

print('splitting data into training and testing sets')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

# print('fitting training data')
# nb = SGDClassifier(loss='log')


text_clf = Pipeline([
	('vect', HashingVectorizer(stop_words='english')),
	('tfidf', TfidfTransformer()),
	('clf', SGDClassifier(loss='modified_huber')),
])
text_clf.fit(X_train, y_train)
preds1 = text_clf.predict(X_test)

predict = pd.DataFrame()
predict['stars']=y_test
predict['stars_sgd_mh']=preds1
print(accuracy_score(y_test, preds1))


text_clf = Pipeline([
	('vect', HashingVectorizer(stop_words='english')),
	('tfidf', TfidfTransformer()),
	('clf', LinearSVC()),
])
text_clf.fit(X_train, y_train)
preds2 = text_clf.predict(X_test)
predict['stars_svc']=preds2

print(accuracy_score(y_test, preds2))

predict["stars_avg"] = predict[['stars_sgd_mh', 'stars_svc']].mean(axis=1)


predict.to_csv('prediction.csv')
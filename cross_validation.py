import pandas as pd
from sklearn.linear_model import LogisticRegression 
from sklearn.model_selection import KFold, cross_val_predict
from sklearn.metrics import accuracy_score

yelp = pd.read_csv('./datashort.csv')

X = yelp['sentiment_score']
y = yelp['stars']

#predict = pd.read_csv('./dataToPredict.csv')

# X_test = predict['text']



nb = LogisticRegression()
k_fold = KFold(n_splits=3)

preds = cross_val_predict(nb, X, y, cv=k_fold, n_jobs=-1)




# predict['stars']=preds
# predict.drop('business_id', axis=1, inplace=True)
# predict.drop('cool', axis=1, inplace=True)
# predict.drop('date', axis=1, inplace=True)
# predict.drop('funny', axis=1, inplace=True)
# predict.drop('text', axis=1, inplace=True)
# predict.drop('useful', axis=1, inplace=True)
# predict.drop('user_id', axis=1, inplace=True)
# predict.to_csv('prediction.csv')

print(accuracy_score(y, preds))
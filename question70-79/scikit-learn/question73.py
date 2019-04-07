#coding:utf-8

import numpy as np
from scipy import io
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib
from question71 import makeStoplist
from question72 import extractFeaturesFromFile


ENCODING = "cp1252"

def learn():

	stoplist = makeStoplist()
	features = extractFeaturesFromFile(stoplist=stoplist)
	vectorizer = TfidfVectorizer(encoding=ENCODING)
	X_train = vectorizer.fit_transform([" ".join(feature[1:]) for feature in features])
	y_train = np.zeros(len(features))
	for i in range(len(features)):
		if features[i][0] == "+1":
			y_train[i] = 1
	clf = LogisticRegression()
	clf.fit(X_train, y_train)

	io.savemat("X_train", {"X_train": X_train})
	np.save("y_train", y_train)
	joblib.dump(vectorizer, "tfidf.vec")
	joblib.dump(clf, "logreg.clf")


if __name__ == "__main__":
	learn()
	print("finish")

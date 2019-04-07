#coding:utf-8

import sys
from sklearn.externals import joblib
from question71 import makeStoplist
from question72 import extractFeaturesFromString
from logreg import LogisticRegression

if __name__ == "__main__":

	vectorizer = joblib.load("tfidf.vec")
	clf = LogisticRegression("logreg")
	stoplist = makeStoplist()
	while True:
		test = input()
		test = extractFeaturesFromString(test, stoplist)
		print(["-1", "+1"][clf.predict(vectorizer.transform([" ".join(test)]))[0]])
		sys.stdout.flush()

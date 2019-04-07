#coding:utf-8

import sys
from sklearn.externals import joblib
from question71 import makeStoplist
from question72 import extractFeaturesFromString


if __name__ == "__main__":

	vectorizer = joblib.load("tfidf.vec")
	clf = joblib.load("logreg.clf")
	stoplist = makeStoplist()
	while True:
		test = input()
		test = extractFeaturesFromString(test, stoplist)
		print(["-1", "+1"][int(clf.predict(vectorizer.transform([" ".join(test)]))[0])])
		sys.stdout.flush()

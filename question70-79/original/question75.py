#coding:utf-8

from sklearn.externals import joblib
from logreg import LogisticRegression


ENCODING = "cp1252"

if __name__ == "__main__":

	vectorizer = joblib.load("tfidf.vec")
	clf = LogisticRegression("logreg")
	terms = vectorizer.get_feature_names()
	index_list = list(range(len(terms)))
	index_list.sort(key=lambda i:clf.coef_[i])

	print("top 10")
	for i in index_list[:-11:-1]:
		print(terms[i], clf.coef_[i])

	print("")
	
	print("worst 10")
	for i in index_list[:10]:
		print(terms[i], clf.coef_[i])

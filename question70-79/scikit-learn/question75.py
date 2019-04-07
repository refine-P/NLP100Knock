#coding:utf-8

from sklearn.externals import joblib


ENCODING = "cp1252"

if __name__ == "__main__":

	vectorizer = joblib.load("tfidf.vec")
	clf = joblib.load("logreg.clf")
	terms = vectorizer.get_feature_names()
	index_list = list(range(len(terms)))
	index_list.sort(key=lambda i:clf.coef_[0][i])

	print("top 10")
	for i in index_list[:-11:-1]:
		print(terms[i], clf.coef_[0, i])

	print("")
	
	print("worst 10")
	for i in index_list[:10]:
		print(terms[i], clf.coef_[0, i])

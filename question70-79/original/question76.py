#coding:utf-8

import numpy as np 
from scipy import io
from sklearn.externals import joblib
from logreg import LogisticRegression


if __name__ == "__main__":
	X_train = io.loadmat("X_train")["X_train"]
	X_train = X_train.tocsr() #疎行列の種類の変更(tfidfVectorizerで出力されるものと同じものにする)
	y_train = np.load("y_train.npy")
	clf = LogisticRegression("logreg")
	y_predict = clf.predict(X_train)
	probs = clf.predict_proba(X_train)
	labels = ["-1", "+1"]
	print("正解ラベル\t予測ラベル\t予測確率(+1)")
	for (train, pred, prob) in zip(y_train, y_predict, probs):
		print("%s\t%s\t%s" % (labels[int(train)], labels[int(pred)], prob))

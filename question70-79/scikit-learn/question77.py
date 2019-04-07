#coding:utf-8

import numpy as np
from scipy import io
from sklearn.externals import joblib
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


if __name__ == "__main__":
	X_train = io.loadmat("X_train")["X_train"]
	X_train = X_train.tocsr() #疎行列の種類の変更(tfidfVectorizerで出力されるものと同じものにする)
	y_train = np.load("y_train.npy")
	clf = joblib.load("logreg.clf")
	y_predict = clf.predict(X_train)
	print("正解率: %f" % accuracy_score(y_train, y_predict))
	print("適合率: %f" % precision_score(y_train, y_predict))
	print("再現率: %f" % recall_score(y_train, y_predict))
	print("F1スコア: %f" % f1_score(y_train, y_predict))

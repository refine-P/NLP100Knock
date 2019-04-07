#coding:utf-8

import time

import numpy as np
from scipy import io
from sklearn.externals import joblib
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from logreg import LogisticRegression


if __name__ == "__main__":
	X_train = io.loadmat("X_train")["X_train"]
	X_train = X_train.tocsr() #疎行列の種類の変更(tfidfVectorizerで出力されるものと同じものにする)
	y_train = np.load("y_train.npy")
	kf = KFold(n_splits=5)

	start = time.time()
	for (i, (train, test)) in enumerate(kf.split(X_train), start=1):
		clf = LogisticRegression()
		clf.fit(X_train[train], y_train[train])		
		y_predict = clf.predict(X_train[test])
		y_test = y_train[test]
		print("Fold %d" % i)
		print("正解率: %f" % accuracy_score(y_test, y_predict))
		print("適合率: %f" % precision_score(y_test, y_predict))
		print("再現率: %f" % recall_score(y_test, y_predict))
		print("F1スコア: %f" % f1_score(y_test, y_predict))
		print("")
	elapsed_time = time.time() - start
	print(str(elapsed_time) + "[sec]")

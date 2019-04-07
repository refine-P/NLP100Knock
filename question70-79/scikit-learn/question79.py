#coding:utf-8

import numpy as np
from scipy import io
from sklearn.externals import joblib
from sklearn.metrics import precision_score, recall_score
import matplotlib.pyplot as plt


def predictWithThreshold(clf, X_train, threshold):

	y_predict = np.vectorize(lambda p:1 if p >= threshold else 0)(clf.predict_proba(X_train)[:, 1])
	return y_predict


if __name__ == "__main__":
	X_train = io.loadmat("X_train")["X_train"]
	X_train = X_train.tocsr() #疎行列の種類の変更(tfidfVectorizerで出力されるものと同じものにする)
	y_train = np.load("y_train.npy")
	clf = joblib.load("logreg.clf")
	threshold_list = [i * 0.05 for i in range(20)]
	precision_list = []
	recall_list = []
	for threshold in threshold_list:
		y_predict = predictWithThreshold(clf, X_train, threshold)
		precision_list.append(precision_score(y_train, y_predict))
		recall_list.append(recall_score(y_train, y_predict))

	plt.plot(threshold_list, precision_list, label = "precision", color = "red")
	plt.plot(threshold_list, recall_list, label = "recall", color = "blue")

	plt.xlabel("threshold")
	plt.ylabel("rate")
	plt.xlim(0.0 , 1.0)
	plt.ylim(0,1)
	plt.title("logistic_regresssion")
	plt.legend(loc = 3)

	plt.show()

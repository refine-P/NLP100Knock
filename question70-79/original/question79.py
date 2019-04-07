#coding:utf-8

import numpy as np
from scipy import io
from sklearn.externals import joblib
from sklearn.metrics import precision_score, recall_score
from logreg import LogisticRegression
import matplotlib.pyplot as plt


if __name__ == "__main__":
	X_train = io.loadmat("X_train")["X_train"]
	X_train = X_train.tocsr() #疎行列の種類の変更(tfidfVectorizerで出力されるものと同じものにする)
	y_train = np.load("y_train.npy")
	clf = LogisticRegression("logreg")
	
	#thresholdに応じたprecisionとrecallの変化をプロット
	threshold_list = [i * 0.05 for i in range(20)]
	precision_list = []
	recall_list = []
	for threshold in threshold_list:
		y_predict = clf.predict(X_train, threshold)
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

	#precision-recall curveをプロット
	from sklearn.metrics import precision_recall_curve
	precision, recall, thresholds = precision_recall_curve(y_train, clf.predict_proba(X_train))
	print(len(thresholds))
	plt.clf()
	plt.plot(recall, precision, label='Precision-Recall curve')
	plt.xlabel('Recall')
	plt.ylabel('Precision')
	plt.ylim([0.0, 1.05])
	plt.xlim([0.0, 1.0])
	plt.title('Precision-Recall curve')
	plt.legend(loc="lower left")
	plt.show()

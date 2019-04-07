#coding:utf-8

import numpy as np
from sklearn.metrics import accuracy_score
import sys
import json

def sigmoid(z):
	return 1.0 / (1.0 + np.exp(-z))

class LogisticRegression:

	def __init__(self, clf_name=None):
		if clf_name is None:
			self.coef_ = None
			self.bias_ = None
		else:
			self.load(clf_name)

	def save(self, clf_name):
		if self.coef_ is None or self.bias_ is None:
			sys.exit("construct a classifier!")
		else:
			clf_dict = {}
			clf_dict["bias_"] = self.bias_
			clf_dict["coef_"] = "%s.npy" % clf_name
			with open("%s.json" % clf_name, "w") as f:
				json.dump(clf_dict, f, indent="\t")

	def load(self, clf_name):
		with open("%s.json" % clf_name) as f:
			clf_json = json.load(f)
		self.bias_ = float(clf_json["bias_"])
		self.coef_ = np.load(clf_json["coef_"])

	#参考(http://gihyo.jp/dev/serial/01/machine-learning/0020?page=2)
	def fit(self, X, y):
		#重みベクトルと定数項を別々に計算
		self.coef_ = np.zeros(X.shape[1])
		self.bias_ = 0
		eta = 0.1
		for i in range(50):
			for n in np.random.permutation(X.shape[0]):
				x = X.getrow(n) #こっちのほうが速い?
				d = eta * (self.predict_proba(x)[0] - y[n])
				grad = d * x.toarray().ravel() #1次元ベクトルに揃えてからかける
				if max(np.max(np.absolute(grad)), d) < 1e-4: return		
				self.coef_ -= grad
				self.bias_ -= d
			eta *= 0.9

	def predict_proba(self, X):
		return sigmoid(self.bias_ + X.dot(self.coef_))

	def predict(self, X, threshold=0.5):
		return np.vectorize(lambda p:1 if p >= threshold else 0)(self.predict_proba(X))
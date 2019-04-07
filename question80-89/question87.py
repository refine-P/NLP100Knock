#coding:utf-8

import pickle
import numpy as np
from scipy.spatial.distance import cosine

def cos_sim(x, y):

	if (x == 0).all() or (y == 0).all():
		return -1
	else:
		return 1 - cosine(x, y)


if __name__ == "__main__":

	X_svd = np.load('X_svd_r100.npy')

	word_dict = None
	with open('word_dict_r100.pkl', 'rb') as f:
		word_dict = pickle.load(f)

	#参考(https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.cosine.html)
	print(cos_sim(X_svd[word_dict["United_States"]], X_svd[word_dict["U.S"]]))

#coding:utf-8

import pickle
import numpy as np


if __name__ == "__main__":

	X_svd = np.load('X_svd_r100.npy')

	word_dict = None
	with open('word_dict_r100.pkl', 'rb') as f:
		word_dict = pickle.load(f)

	print(X_svd[word_dict["United_States"]])
	
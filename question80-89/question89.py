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
	print("ready")

	y = X_svd[word_dict["Spain"]] - X_svd[word_dict["Madrid"]] + X_svd[word_dict["Athens"]]
	del word_dict
	sims = [cos_sim(x, y) for x in X_svd]
	del X_svd
	print("calc")

	word_list = None
	with open('word_list_r100.pkl', 'rb') as f:
		word_list = pickle.load(f)

	indices = list(range(len(word_list)))
	indices.sort(key=lambda i: -sims[i]) #降順にソート

	for idx in indices[:15]: 
		print(word_list[idx], sims[idx])

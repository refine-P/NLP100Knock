#coding:utf-8

import pickle
import numpy as np
from sklearn.neighbors import NearestNeighbors


if __name__ == "__main__":

	X_svd = np.load('../question80-89/X_svd_r100.npy')
	#コサイン類似度はalgorithm='brute'以外だとダメ
	neigh = NearestNeighbors(n_neighbors = 1, algorithm='brute', metric='cosine')
	neigh.fit(X_svd)

	word_dict = None
	with open('../question80-89/word_dict_r100.pkl', 'rb') as f:
		word_dict = pickle.load(f)

	word_list = None
	with open('../question80-89/word_list_r100.pkl', 'rb') as f:
		word_list = pickle.load(f)

	with open("analogy_data_family.txt", "r", encoding='utf-8') as fr, open("analogy_result_family_85.txt", "w", encoding='utf-8') as fw:
		for line in fr:
			words = line.split()
			try:
				vec = X_svd[word_dict[words[1]]] - X_svd[word_dict[words[0]]] + X_svd[word_dict[words[2]]]
				dist, ind = neigh.kneighbors([vec])
				result = "%s\t%s\n" % (" ".join(words), "%s %f" % (word_list[ind[0][0]], 1 - dist[0][0]))
			except:
				result = "%s\tfailure...\n" % " ".join(words)
			fw.write(result)

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

	X_svd = np.load('../question80-89/X_svd_r100.npy')

	word_dict = None
	with open('../question80-89/word_dict_r100.pkl', 'rb') as f:
		word_dict = pickle.load(f)

	with open("combined.tab", "r", encoding='utf-8') as fr, open("353_result_85.txt", "w", encoding='utf-8') as fw:
		for line in fr.readlines()[1:]:
			words = line.split()
			try:
				v1 = X_svd[word_dict[words[0]]]
				v2 = X_svd[word_dict[words[1]]]
				sim = cos_sim(v1, v2)
				result = "%s\t%f\n" % (" ".join(words[0:2]), sim)
			except:
				result = "%s\t-1\n" % " ".join(words[0:2])
			fw.write(result)

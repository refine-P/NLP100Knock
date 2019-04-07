#coding:utf-8

from time import time
import pickle
import numpy as np
from scipy.sparse import csr_matrix
from scipy import io
import sys


def getWordList(corpus="tokens2_r100.txt"):

	res = set()
	with open(corpus, encoding='utf-8') as f:
		for line in f:
			res |= set(line.split())
	res = list(res)
	return res


#key=word,value=indexのdictを作成
def toWordDict(word_list):
	return {w: i for i, w in enumerate(word_list)}

#時間はtimeでメモリはmemory_profilerでそれぞれ別々に測定
#dok only: 1272.148000[sec], (max)2651.516 MiB
#dok+csr(per 100000): 1532.076000[sec], (max)257.957 MiB 
#csr only(per 1000000): 76.962000[sec], 254.539 MiB
#pandasを使ってみたが性能に変化はなかった(ので省略)
#@profile
def calcFrequency(word_dict, context_path="context_r100.txt"):

	n = len(word_dict)
	res = csr_matrix((n, n), dtype=np.int32)
	row = []
	col = []
	with open(context_path, encoding='utf-8') as f:
		for line in f:
			t, c = line.split()
			row.append(word_dict[t])
			col.append(word_dict[c])
			if len(row) == 1000000:
				res += csr_matrix((np.ones(len(row), dtype=np.int32), (row, col)), shape=(n, n), dtype=np.int32)
				row = []
				col = []

	res += csr_matrix((np.ones(len(row), dtype=np.int32), (row, col)), shape=(n, n), dtype=np.int32)
	return res


if __name__ == "__main__":

	word_list = getWordList()
	word_dict = toWordDict(word_list)	

	print("get word_dict")
	sys.stdout.flush()

	s=time()
	freq = calcFrequency(word_dict)
	print("%f[sec]" % (time() - s))

	print("finish calc")
	sys.stdout.flush()

	with open('word_list_r100.pkl', 'wb') as f:
		pickle.dump(word_list, f)

	with open('word_dict_r100.pkl', 'wb') as f:
		pickle.dump(word_dict, f)

	io.savemat("freq_r100", {"freq": freq})

	print("finish save")

#coding:utf-8

import math
from time import time
import numpy as np
from scipy import io
from scipy.sparse import csr_matrix
import sys

"""
参考
http://hamukazu.com/2014/06/04/scipy-sparse-universal-function/
"""

#before(use dok): 121.792000[sec], (max)3906.613 MiB
#after(use csr only): 1.518000[sec], (max)202.387 MiB 
if __name__ == "__main__":

	X = io.loadmat('freq_r100')['freq'] #csc format
	csum_list = X.sum(axis=0).getA1()
	X = X.tocsr()
	tsum_list = X.sum(axis=1).getA1()
	N = tsum_list.sum()
	print("ready")

	s=time()

	#f(t, c) < 10の場合X_tc=0にする処理
	X.data[X.data < 10] = 0
	X.eliminate_zeros() #X_tc=0にしてもX.dataには0が残っているので0を除去

	#PPMIの計算
	#1. log(f(t, c)) + log(N)を計算
	X.data = np.log(X.data) + math.log(N)

	#2. 1.からlog(f(t, *))を引く
	for i, tsum in enumerate(tsum_list):
		if tsum != 0:
			X.data[X.indptr[i]:X.indptr[i + 1]] -= math.log(tsum)
	del tsum_list

	#3. 2.からlog(f(*, c))を引く
	X=X.tocsc()
	for j, csum in enumerate(csum_list):
		if csum != 0:
			X.data[X.indptr[j]:X.indptr[j + 1]] -= math.log(csum)
	del csum_list

	#4. 値が負となる要素は値を0に変える
	X.data[X.data < 0] = 0
	X.eliminate_zeros()
	print("calc matrix")

	io.savemat('X_r100', {'X':X})
	print("save matrix")

	print("%f[sec]" % (time() - s))

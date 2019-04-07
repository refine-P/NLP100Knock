#coding:utf-8

from time import time
import numpy as np
from scipy import io
from sklearn.decomposition import TruncatedSVD
from sklearn.externals import joblib

#randomized: 113.567000[sec], (average)3.7GB
#arpack: 363.994000[sec], (average)1.8GB
if __name__ == "__main__":

	X = io.loadmat('X_r100')['X']
	s=time()
	svd = TruncatedSVD(n_components=300)
	X_svd = svd.fit_transform(X)
	del X #メモリを食うので用済みなら削除
	print("%f[sec]" % (time() - s))
	print("calc SVD")

	np.save('X_svd_r100', X_svd)
	joblib.dump(svd, 'svd_r100.jl')
	print("save")

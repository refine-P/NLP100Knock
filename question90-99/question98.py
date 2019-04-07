#coding:utf-8

#Windowsだと警告が出るが特に問題がないらしいのでこれで握りつぶす
#参考(http://stackoverflow.com/questions/41658568/chunkize-warning-while-installing-gensim)
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')

from gensim.models.word2vec import Word2Vec
from scipy.cluster.hierarchy import ward, dendrogram
import matplotlib.pyplot as plt
from question96 import extractCountryVectors


if __name__ == "__main__":

	model = Word2Vec.load("word2vec.model")
	country_list, country_vectors = extractCountryVectors(model, "../question80-89/country_list.txt")

	z = ward(country_vectors)
	dendrogram(z, labels=country_list, leaf_font_size=8)
	plt.show()

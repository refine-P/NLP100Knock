#coding:utf-8

#Windowsだと警告が出るが特に問題がないらしいのでこれで握りつぶす
#参考(http://stackoverflow.com/questions/41658568/chunkize-warning-while-installing-gensim)
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')

from gensim.models.word2vec import Word2Vec
from sklearn.cluster import KMeans
from question96 import extractCountryVectors


if __name__ == "__main__":

	model = Word2Vec.load("word2vec.model")
	country_list, country_vectors = extractCountryVectors(model, "../question80-89/country_list.txt")

	kmeans = KMeans(n_clusters=5)
	kmeans.fit(country_vectors)

	print("labels:")
	for country, label in zip(country_list, kmeans.labels_):
		print("%s\t%d" % (country, label))

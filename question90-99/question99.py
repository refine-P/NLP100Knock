#coding:utf-8

#Windowsだと警告が出るが特に問題がないらしいのでこれで握りつぶす
#参考(http://stackoverflow.com/questions/41658568/chunkize-warning-while-installing-gensim)
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')

from gensim.models.word2vec import Word2Vec
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from question96 import extractCountryVectors


if __name__ == "__main__":

	model = Word2Vec.load("word2vec.model")
	country_list, country_vectors = extractCountryVectors(model, "../question80-89/country_list.txt")

	tsne = TSNE()
	result = tsne.fit_transform(country_vectors)

	fig, ax = plt.subplots()
	ax.scatter(result[:, 0], result[:, 1])
	for idx, label in enumerate(country_list):
		ax.annotate(label, xy=(result[idx, 0], result[idx, 1]))
	plt.show()

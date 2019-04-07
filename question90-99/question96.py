#coding:utf-8

#Windowsだと警告が出るが特に問題がないらしいのでこれで握りつぶす
#参考(http://stackoverflow.com/questions/41658568/chunkize-warning-while-installing-gensim)
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')

import numpy as np
from gensim.models.word2vec import Word2Vec


def extractCountryVectors(model, country_list_path):

	with open(country_list_path, encoding='utf-8') as fc: 
		country_list = ["_".join(country.rstrip().split()) for country in fc]

	country_list = [country for country in country_list if country in model.wv]
	country_vectors = np.array([model.wv[country] for country in country_list])
	return country_list, country_vectors


if __name__ == "__main__":

	model = Word2Vec.load("word2vec.model")
	country_list, country_vectors = extractCountryVectors(model, "../question80-89/country_list.txt")

	for country, vector in zip(country_list, country_vectors):
		print("%s:" % country)
		print(vector)

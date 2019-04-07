#coding:utf-8

#Windowsだと警告が出るが特に問題がないらしいのでこれで握りつぶす
#参考(http://stackoverflow.com/questions/41658568/chunkize-warning-while-installing-gensim)
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')

from gensim.models.word2vec import Word2Vec


if __name__ == "__main__":

	model = Word2Vec.load("word2vec.model")

	for factor in model.most_similar(positive=["England"]):
		print("%s %f" % factor)

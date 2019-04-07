#coding:utf-8

#Windowsだと警告が出るが特に問題がないらしいのでこれで握りつぶす
#参考(http://stackoverflow.com/questions/41658568/chunkize-warning-while-installing-gensim)
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')

from gensim.models.word2vec import LineSentence, Word2Vec


if __name__ == "__main__":

	sentences = LineSentence("../question80-89/tokens2_r100.txt")
	model = Word2Vec(sentences, size=300)
	model.save("word2vec.model")
#coding:utf-8

#Windowsだと警告が出るが特に問題がないらしいのでこれで握りつぶす
#参考(http://stackoverflow.com/questions/41658568/chunkize-warning-while-installing-gensim)
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')

from gensim.models.word2vec import Word2Vec


if __name__ == "__main__":

	model = Word2Vec.load("word2vec.model")

	with open("combined.tab", "r", encoding='utf-8') as fr, open("353_result.txt", "w", encoding='utf-8') as fw:
		for line in fr.readlines()[1:]:
			words = line.split()
			try:
				sim = model.similarity(words[0], words[1])
				result = "%s\t%f\n" % (" ".join(words[0:2]), sim)
			except:
				result = "%s\t-1\n" % " ".join(words[0:2])
			fw.write(result)

#coding:utf-8

#Windowsだと警告が出るが特に問題がないらしいのでこれで握りつぶす
#参考(http://stackoverflow.com/questions/41658568/chunkize-warning-while-installing-gensim)
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')

from gensim.models.word2vec import Word2Vec


if __name__ == "__main__":

	model = Word2Vec.load("word2vec.model")

	with open("analogy_data_family.txt", "r", encoding='utf-8') as fr, open("analogy_result_family.txt", "w", encoding='utf-8') as fw:
		for line in fr:
			words = line.split()
			try:
				sim = model.most_similar(positive=words[1:3], negative=[words[0]], topn=1)
				result = "%s\t%s\n" % (" ".join(words), "%s %f" % sim[0])
			except:
				result = "%s\tfailure...\n" % " ".join(words)
			fw.write(result)

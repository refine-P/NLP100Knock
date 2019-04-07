#coding:utf-8

from question50 import splitText
from question51 import cutSentence
from stemming.porter2 import stem

if __name__ == "__main__":

	for sentence in splitText():
		for word in cutSentence(sentence):
			print(word + "\t" + stem(word))
		print("")
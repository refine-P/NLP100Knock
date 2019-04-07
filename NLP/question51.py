#coding:utf-8

import re
from question50 import splitText

def removeSymbol(word):
	if word == "e.g.":
		return word

	res = word

	res = re.sub(r"[!-/:-@[-`{-~]+$" , '', res)
	res = re.sub(r"^[!-/:-@[-`{-~]+" , '', res)

	return res

def cutSentence(sentence):

	#空白で区切る
	res = sentence.split(' ')

	#記号を除去
	res = [removeSymbol(w) for w in res]

	#空文字を除去
	res = [b for b in res if b!='']

	return res


if __name__ == "__main__":
	
	for sentence in splitText():
		for word in cutSentence(sentence):
			print(word)
		print("")
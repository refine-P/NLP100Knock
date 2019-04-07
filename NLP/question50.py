#coding:utf-8

import re
from itertools import chain

def splitText(text_path="nlp.txt"):

	pat = re.compile(r"(?<=[.;:?!])\s(?=[A-Z])")

	text = open(text_path, "r", encoding='utf-8').read()

	#問題文通りに区切る
	res = pat.split(text)

	#改行文字が残っていた場合、文の区切りとみなす
	res = [s.split('\n') for s in res]

	#listをflattenする(http://d.hatena.ne.jp/xef/20121027/p2)
	res = list(chain.from_iterable(res))

	#空文字を除去(もとの文章から改行だけの文を削除するのに等しい)
	res = [b for b in res if b!='']
	
	return res


if __name__ == "__main__":
	for line in splitText():
		print(line)
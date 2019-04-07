#coding:utf-8

from collections import Counter

#以下のコマンドで出現頻度の高い単語をストップワードとして書き出す
#python word_freq.py | cut -f1 -d' ' > stopwords.txt

ENCODING = "cp1252"

if __name__ == "__main__":

	words = []

	with open("sentiment.txt", "r", encoding=ENCODING) as f:
		for line in f:
			words.extend(line.rstrip().split())

	counter = Counter(words)
	del counter['+1']
	del counter['-1']

	for word, count in counter.most_common(100):
		print(word, count)
#coding:utf-8

import matplotlib.pyplot as plt

"""
matplotlib 日本語表示
http://www.sakito.com/2012/01/matplotlib.html
http://qiita.com/RioKKH/items/036c340afa27a12a6e20
"""

if __name__ == "__main__":
	words = []
	freq = []
	cnt = 0
	for line in open("word_freq.txt", "r", encoding='utf-8'):
		if cnt == 10:
			break

		key, value = line.split(' ')
		value = int(value)
		words.append(key)
		freq.append(value)
		cnt += 1

	X = range(10)
	plt.bar(X, freq, align='center')
	plt.xticks(X, words)
	plt.xlabel("word")
	plt.ylabel("freq")
	plt.show()
	
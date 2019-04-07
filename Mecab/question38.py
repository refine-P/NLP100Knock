#coding:utf-8

import matplotlib.pyplot as plt

if __name__ == "__main__":
	freq = []
	for line in open("word_freq.txt", "r", encoding='utf-8'):
		key, value = line.split(' ')
		value = int(value)
		freq.append(value)

	plt.hist(freq, bins=range(0, 21)) #20回より多く出現する単語は殆ど無いので排除
	plt.xlabel("freq")
	plt.ylabel("word")
	plt.show()

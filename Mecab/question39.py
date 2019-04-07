#coding:utf-8

import matplotlib.pyplot as plt

if __name__ == "__main__":
	X = []
	Y = []
	rank = 0
	for line in open("word_freq.txt", "r", encoding='utf-8'):
		rank += 1
		key, value = line.split(' ')
		value = int(value)
		X.append(rank)
		Y.append(value)

	plt.xscale("log")
	plt.yscale("log")
	plt.plot(X, Y) 
	plt.xlabel("log(rank)")
	plt.ylabel("log(freq)")
	plt.show()

#coding:utf-8

import random

#データの文字コードがUTF-8ではないらしい(http://qiita.com/segavvy/items/0e91fe02088b875a386a)
ENCODING = "cp1252"

if __name__ == "__main__":

	data = []

	pos = 0
	with open("rt-polaritydata/rt-polaritydata/rt-polarity.pos", "r", encoding=ENCODING) as f:
		for line in f:
			pos += 1
			data.append("+1 " + line)

	neg = 0
	with open("rt-polaritydata/rt-polaritydata/rt-polarity.neg", "r", encoding=ENCODING) as f:
		for line in f:
			neg += 1
			data.append("-1 " + line)

	random.shuffle(data)

	with open("sentiment.txt", "w", encoding=ENCODING) as f:
		for factor in data:
			f.write(factor)

	print("positive:", pos)
	print("negative:", neg)
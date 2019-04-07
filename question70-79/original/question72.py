#coding:utf-8

from stemming.porter2 import stem
from question71 import makeStoplist, isIncludedInStoplist

ENCODING = "cp1252"

def extractFeaturesFromString(sentence, stoplist):
	res = []
	for word in sentence.strip().split():
		if isIncludedInStoplist(word, stoplist):
			continue
		res.append(stem(word))
	return res	


def extractFeaturesFromFile(data_file="sentiment.txt", stoplist=None):
	res = []
	if stoplist is None:
		stoplist = makeStoplist()
	with open(data_file, "r", encoding=ENCODING) as f:
		for line in f:
			res.append(extractFeaturesFromString(line, stoplist))
	return res
	


if __name__ == "__main__":
	features = extractFeaturesFromFile()
	for feature in features:
		print(" ".join(feature))

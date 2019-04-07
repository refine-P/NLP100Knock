#coding:utf-8

import random

if __name__ == "__main__":

	with open("tokens2_r100.txt", "r", encoding='utf-8') as fr, open("context_r100.txt", "w", encoding='utf-8') as fw:
		for line in fr:
			words = line.split()
			for i in range(len(words)):
				t = words[i]
				d = random.randint(1, 5)
				for c in words[max(0, i - d):i]:
					fw.write("%s\t%s\n" % (t, c))
				for c in words[i + 1:min(i + d + 1, len(words))]:
					fw.write("%s\t%s\n" % (t, c))

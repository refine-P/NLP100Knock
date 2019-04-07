#coding:utf-8

import re
from Morph import Morph

def inputCabochaOnlyMorpheme():
	#Cabochaのフォーマット
	#http://qiita.com/nezuq/items/f481f07fc0576b38e81d
	res = []
	p = re.compile(r"[,\t]")
	morphs = []
	for line in open("neko.txt.cabocha", "r", encoding='utf-8'):
		if line[0:2] == "* ":
			continue

		m = list(p.split(line.rstrip()))
		if len(m) > 1:
			tmp = Morph(m[0], m[7], m[1], m[2])
			morphs.append(tmp)

		else:
			res.append(morphs)
			morphs = []

	return res

if __name__ == "__main__":
	neko_list = inputCabochaOnlyMorpheme()
	for morpheme in neko_list[2]: 
		print(morpheme)

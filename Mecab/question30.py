#coding:utf-8

import re

def inputMecab():
	#形態素のフォーマット
	#表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
	res = []
	p = re.compile(r"[,\t]")
	morphs = []
	for line in open("neko.txt.mecab", "r", encoding="utf-8"):
		m = list(p.split(line.rstrip()))
		if len(m) > 1:
			tmp = {}
			tmp["surface"] = m[0]
			tmp["base"] = m[7]
			tmp["pos"] = m[1]
			tmp["pos1"] = m[2]
			morphs.append(tmp)

		else:
			if len(morphs) > 0:
				res.append(morphs)
				morphs = []
	return res

if __name__ == "__main__":
	neko_list = inputMecab()
	print(neko_list[1])
	for morphs in neko_list[:2]:
		for morpheme in morphs:
			print(morpheme["surface"], morpheme["base"], morpheme["pos"], morpheme["pos1"])
			
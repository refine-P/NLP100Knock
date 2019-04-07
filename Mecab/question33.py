#coding:utf-8

from question30 import inputMecab

if __name__ == "__main__":
	neko_list = inputMecab()
	f = open("noun_sahen.txt", "w", encoding='utf-8')
	for morphs in neko_list:
		for morpheme in morphs:
			if morpheme["pos"] == "名詞" and morpheme["pos1"] == "サ変接続":
				f.write(morpheme["surface"] + "\n")
				
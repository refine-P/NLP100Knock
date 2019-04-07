#coding:utf-8

from question30 import inputMecab

if __name__ == "__main__":
	neko_list = inputMecab()
	f = open("noun_longest.txt", "w", encoding='utf-8')
	nouns = []
	for morphs in neko_list:
		for morpheme in morphs:
			if morpheme["pos"] == "名詞":
				nouns.append(morpheme["surface"])
			else:
				if len(nouns) > 1:
					f.write("".join(nouns) + "\n")
				nouns = []

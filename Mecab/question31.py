#coding:utf-8

from question30 import inputMecab

if __name__ == "__main__":
	neko_list = inputMecab()
	f = open("verb_surface.txt", "w", encoding="utf-8")
	for morphs in neko_list:
		for morpheme in morphs:
			if morpheme["pos"] == "動詞":
				f.write(morpheme["surface"] + "\n")

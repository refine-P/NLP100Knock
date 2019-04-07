#coding:utf-8

from question30 import inputMecab

if __name__ == "__main__":
	neko_list = inputMecab()
	f = open("noun_no.txt", "w", encoding='utf-8')
	for morphs in neko_list:
		for i in range(len(morphs) - 2):
			if morphs[i]["pos"] != "名詞":
				continue
			if morphs[i + 1]["surface"] != "の":
				continue
			if morphs[i + 2]["pos"] != "名詞":
				continue
			f.write(morphs[i]["surface"] + morphs[i + 1]["surface"] + morphs[i + 2]["surface"] + "\n")

#coding:utf-8

from question30 import inputMecab

if __name__ == "__main__":
	neko_list = inputMecab()
	f = open("word_freq.txt", "w", encoding='utf-8')
	word_freq = {}
	for morphs in neko_list:
		for morpheme in morphs:
			if morpheme["surface"] in word_freq:
				word_freq[morpheme["surface"]] += 1
			else:
				word_freq[morpheme["surface"]] = 1

	for key, value in sorted(word_freq.items(), key=lambda x: -x[1]):
		f.write(key + " " + str(value) + "\n")

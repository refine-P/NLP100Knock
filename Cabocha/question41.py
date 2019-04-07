#coding:utf-8

import re
from Morph import Morph
from Chunk import Chunk

def inputCabocha(cabocha_result_file="neko.txt.cabocha"):
	#Cabochaのフォーマット
	#http://qiita.com/nezuq/items/f481f07fc0576b38e81d
	res = []
	chunks = {}
	idx = -1
	p = re.compile(r"[,\t]")
	for line in open(cabocha_result_file, "r", encoding='utf-8'):
		
		if line[0:2] == "* ":
			m = line.split(' ')
			idx = int(m[1])
			dst = int(m[2][:-1])

			if idx not in chunks:
				chunks[idx] = Chunk(idx)
			chunks[idx].dst = dst
			chunks[idx].srcs.sort()

			if dst != -1:
				if dst not in chunks:
					chunks[dst] = Chunk(dst)
				chunks[dst].srcs.append(idx)

			continue

		m = list(p.split(line.rstrip()))
		if len(m) > 1:
			morpheme = Morph(m[0], m[7], m[1], m[2])
			chunks[idx].morphs.append(morpheme)

		else:
			chunks = [v for k, v in sorted(chunks.items())] #key=index順にソートしvalueのみを取り出す
			res.append(chunks)
			chunks = {}
			idx = -1
	return res

if __name__ == "__main__":
	neko_list = inputCabocha()
	for chunk in neko_list[7]: 
		print(chunk)			

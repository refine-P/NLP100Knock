#coding:utf-8

from question41 import inputCabocha

if __name__ == "__main__":
	neko_list = inputCabocha()
	f = open("chunk_depend_nv.txt", "w", encoding='utf-8')
	for chunks in neko_list:
		for chunk in chunks:
			for idx in chunk.srcs:
				src = chunks[idx].getChunkSurface()
				dst = chunk.getChunkSurface()
				if src == "" or dst == "":
					continue
				if chunks[idx].hasPos("名詞") and chunk.hasPos("動詞"):
					f.write(src + "\t" + dst + "\n")

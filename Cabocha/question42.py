#coding:utf-8

from question41 import inputCabocha

if __name__ == "__main__":
	neko_list = inputCabocha()
	f = open("chunk_depend.txt", "w", encoding='utf-8')
	for chunks in neko_list:
		for chunk in chunks:
			for idx in chunk.srcs:
				src = chunks[idx].getChunkSurface()
				dst = chunk.getChunkSurface()
				if src == "" or dst == "":
					continue
				f.write(src + "\t" + dst + "\n")

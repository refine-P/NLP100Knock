#coding:utf-8

from question41 import inputCabocha

def buildPathFromNounToRoot(chunks):
	res = []
	for chunk in chunks:
		if not chunk.hasPos("名詞"):
			continue

		path = [chunk] 

		nex = chunk.dst
		while nex != -1:
			path.append(chunks[nex])
			nex = chunks[nex].dst

		res.append(path)

	return res


if __name__ == "__main__":
	neko_list = inputCabocha()
	for path in buildPathFromNounToRoot(neko_list[7]):
		print(" -> ".join([x.getChunkSurface() for x in path]))
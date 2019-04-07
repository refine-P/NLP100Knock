#coding:utf-8

from question41 import inputCabocha
from question48 import buildPathFromNounToRoot

def buildPathBetweenNouns(chunks):
	res = []

	paths = buildPathFromNounToRoot(chunks)

	for i in range(len(paths)):
		for j in range(i + 1, len(paths)):
			path = []

			path1 = paths[i][:]
			path2 = paths[j][:]
			chunk1 = path1[-1]
			chunk2 = path2[-1]
			meet = chunk1
			while chunk1.idx == chunk2.idx:
				meet = chunk1
				path1.pop()
				path2.pop()
				if len(path2) == 0:
					break
				chunk1 = path1[-1]
				chunk2 = path2[-1]

			path.append(path1)
			if len(path2) != 0:
				path.append(path2)
			path.append(meet)
			res.append(path)

	return res

def replaceNoun(chunk, char):
	res = ""
	flag = 0 #0:charへの変換未遂、1:名詞の連接が継続中(名詞句の判定)、2:charへの変換済み
	for morpheme in chunk.morphs:
		if morpheme.pos == "記号":
			continue
		if flag != 2 and morpheme.pos == "名詞":
			if flag == 0:
				res += char
				flag = 1
		else:
			res += morpheme.surface
			if flag == 1:
				flag = 2

	return res


if __name__ == "__main__":
	neko_list = inputCabocha()
	for path in buildPathBetweenNouns(neko_list[7]):
		s = replaceNoun(path[0][0], 'X')

		for chunk in path[0][1:]:
			s += " -> "
			s += chunk.getChunkSurface()
		if len(path) == 2:
			s += " -> "
			s += replaceNoun(path[1], 'Y')
		else:
			s += " | "
			s += replaceNoun(path[1][0], 'Y')
			for chunk in path[1][1:]:
				s += " -> "
				s += chunk.getChunkSurface()
			s += " | "
			s += path[2].getChunkSurface()

		print(s)

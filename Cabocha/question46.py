#coding:utf-8

from question41 import inputCabocha

def sortPattern(pattern):
	idx_list = list(range(len(pattern[1])))
	idx_list.sort(key=lambda i:pattern[1][i])
	pattern[1] = [pattern[1][i] for i in idx_list]
	pattern[2] = [pattern[2][i] for i in idx_list]


def extractVerbCaseInfo(chunks):
	res = []
	for chunk in chunks:
		for morph in chunk.morphs:

			if morph.pos != "動詞":
				continue

			pattern = [morph.base]

			particles = []
			section = []
			for src in chunk.srcs:
				particle = None
				has_case_particle = False

				#1つの文節に複数の助詞が存在する場合は最右のものを優先
				for morph2 in chunks[src].morphs[::-1]:

					if morph2.pos != "助詞":
						continue

					if particle is None:
						particle = morph2.base
						has_case_particle = (morph2.pos1 == "格助詞")

					#1つの文節に複数の助詞が存在する場合は格助詞を優先(優先度は 格助詞 > 最右)
					elif not has_case_particle and morph2.pos1 == "格助詞":
						particle = morph2.base
						has_case_particle = True

					if has_case_particle:
						break

				if particle is not None:
					particles.append(particle)
					section.append(chunks[src].getChunkSurface())

			if len(particles) > 0:
				pattern.append(particles)
				pattern.append(section)
				sortPattern(pattern)

			if len(pattern) > 1:
				res.append(pattern)

			break

	return res

if __name__ == "__main__":
	neko_list = inputCabocha()

	for pattern in extractVerbCaseInfo(neko_list[7]):
		print(pattern[0] + "\t" + " ".join(pattern[1]) + "\t" + " ".join(pattern[2]))
	
#coding:utf-8

"""
UNIXコマンド
cut -f1 light_verb.txt | LC_ALL=C sort -t $'\t' | LC_ALL=C uniq -c | sort -k1 -n -r | head -20
cut -f1,2 light_verb.txt | LC_ALL=C sort -t $'\t' | LC_ALL=C uniq -c | sort -k1 -n -r | head -20
"""

from question41 import inputCabocha

def getSahenPlusWo(chunk):
	for idx in range(len(chunk.morphs) - 1):
		if chunk.morphs[idx].pos != "名詞" or chunk.morphs[idx].pos1 != "サ変接続":
			continue

		if chunk.morphs[idx + 1].pos == "助詞" and chunk.morphs[idx + 1].base == "を":
			return chunk.morphs[idx].base + "を"

	return None


def sortPattern(pattern):
	idx_list = list(range(len(pattern[1])))
	idx_list.sort(key=lambda i:pattern[1][i])
	pattern[1] = [pattern[1][i] for i in idx_list]
	pattern[2] = [pattern[2][i] for i in idx_list]


def mineLightVerb(chunks):
	res = []
	for chunk in chunks:
		sahen_plus_wo = getSahenPlusWo(chunk)
		if sahen_plus_wo is None:
			continue

		if chunk.dst == -1:
			continue

		srcs = chunk.srcs
		for morph in chunks[chunk.dst].morphs:

			if morph.pos != "動詞":
				continue

			pattern = [sahen_plus_wo + morph.base]
			srcs.extend(chunks[chunk.dst].srcs)
			srcs.remove(chunk.idx)
			particles = []
			section = []

			for src in srcs:
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
			"""
			if len(particles) > 0:
				pattern.append(particles)
				pattern.append(section)
				sortPattern(pattern)

			if len(pattern) > 1:
				res.append(pattern)
			"""

			#「サ変接続名詞+を（助詞）」の文節以外に、動詞を含む文節に係る文節がない場合も除去しない
			pattern.append(particles)
			pattern.append(section)
			sortPattern(pattern)
			res.append(pattern)

			break

	return res

if __name__ == "__main__":
	neko_list = inputCabocha()

	"""
	for pattern in mineLightVerb(neko_list[948]):
		print pattern[0] + "\t" + " ".join(pattern[1]) + "\t" + " ".join(pattern[2])
	"""

	f = open("light_verb.txt", "w", encoding='utf-8')

	for chunks in neko_list:
		for pattern in mineLightVerb(chunks):
			f.write(pattern[0] + "\t" + " ".join(pattern[1]) + "\t" + " ".join(pattern[2]) + "\n")
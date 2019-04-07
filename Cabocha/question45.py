#coding:utf-8

"""
UNIXコマンド
cat verb_case_pattern.txt | LC_ALL=C sort -t $'\t' | LC_ALL=C uniq -c | sort -k1 -n -r | head -20
cat verb_case_pattern.txt | grep ^する$'\t' | LC_ALL=C sort -t $'\t' | LC_ALL=C uniq -c | sort -k1 -n -r | head -20
cat verb_case_pattern.txt | grep ^見る$'\t' | LC_ALL=C sort -t $'\t' | LC_ALL=C uniq -c | sort -k1 -n -r | head -20
cat verb_case_pattern.txt | grep ^与える$'\t' | LC_ALL=C sort -t $'\t' | LC_ALL=C uniq -c | sort -k1 -n -r | head -20
"""

from question41 import inputCabocha

def extractVerbCasePattern(chunks):
	res = []
	for chunk in chunks:
		for morph in chunk.morphs:

			if morph.pos != "動詞":
				continue

			pattern = [morph.base]

			particles = []
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

			if len(particles) > 0:
				particles.sort()
				pattern.append(particles)

			if len(pattern) > 1:
				res.append(pattern)

			break

	return res

if __name__ == "__main__":
	neko_list = inputCabocha()

	"""
	for pattern in extractVerbCasePattern(neko_list[7]):
		print(pattern[0] + "\t" + " ".join(pattern[1]))
	"""

	f = open("verb_case_pattern.txt", "w", encoding='utf-8')

	for chunks in neko_list:
		for pattern in extractVerbCasePattern(chunks):
			f.write(pattern[0] + "\t" + " ".join(pattern[1]) + "\n")

#coding:utf-8

if __name__ == "__main__":

	with open("enwiki-20150112-400-r100-10576.txt", "r", encoding='utf-8') as fr, open("tokens_r100.txt", "w", encoding='utf-8') as fw:
		for line in fr:
			tokens = []
			for token in line.split():
				token = token.strip(".,!?;:()[]'\"")
				if len(token) > 0:
					tokens.append(token)
			fw.write(" ".join(tokens) + "\n")

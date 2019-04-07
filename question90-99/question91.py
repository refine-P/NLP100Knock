#coding:utf-8


if __name__ == "__main__":

	#ファイルのリンクが切れてるのでhttps://github.com/svn2github/word2vecから入手
	with open("questions-words.txt", "r", encoding='utf-8') as fr, open("analogy_data_family.txt", "w", encoding='utf-8') as fw:

		write_flag = False
		for line in fr:
			line = line.rstrip()

			if line[0] == ':':
				if line[2:] == "family":
					write_flag = True
				elif write_flag:
					break

			elif write_flag:
				fw.write(line + "\n")

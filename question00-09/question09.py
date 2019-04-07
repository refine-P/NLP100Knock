#coding:utf-8

from random import shuffle

def Typoglycemia(str1):
	str1_list = str1.split()
	print(str1_list)
	for i in range(len(str1_list)):
		if len(str1_list[i]) > 4:
			tmp_list = list(str1_list[i])[1:-1]
			shuffle(tmp_list)
			str1_list[i] = str1_list[i][0] + "".join(tmp_list) + str1_list[i][-1]
	return " ".join(str1_list)

str1 = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(Typoglycemia(str1))
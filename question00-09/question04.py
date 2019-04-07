word_list = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.".split()
one_char_list = [i - 1 for i in [1, 5, 6, 7, 8, 9, 15, 16, 19]]
dic = {}
for i in range(len(word_list)):
	if i in one_char_list:
		dic[word_list[i][0]] = i + 1
	else:
		dic[word_list[i][0:2]] = i + 1
print(dic)

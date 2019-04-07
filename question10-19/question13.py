#coding:utf-8

# paste col1.txt col2.txt

col1 = open("col1.txt", encoding='utf-8').readlines()
col2 = open("col2.txt", encoding='utf-8').readlines()

f = open("col.txt", "w", encoding='utf-8')

for i in range(len(col1)):
	f.write(col1[i].rstrip("\r\n") + " " + col2[i])
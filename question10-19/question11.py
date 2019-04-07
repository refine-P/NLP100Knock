#coding:utf-8

# cat hightemp.txt | tr "\t" " "

for line in open("hightemp.txt", encoding='utf-8'):
	print(line.replace('\t',' '), end=' ')
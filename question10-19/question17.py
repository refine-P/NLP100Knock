#coding:utf-8

# cut -f 1 hightemp.txt | sort | uniq

uniq_list = []
for line in open("hightemp.txt", encoding='utf-8'):
	uniq_list.append(line.split()[0])

for factor in set(uniq_list):
	print(factor)
#coding:utf-

# sort -k3nr hightemp.txt

sort_list = [line.split() for line in open("hightemp.txt", encoding='utf-8').readlines()]
sort_list.sort(key=lambda line:float(line[2]), reverse=True)

for line in sort_list:
	print(" ".join(line))
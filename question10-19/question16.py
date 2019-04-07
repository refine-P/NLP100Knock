#coding:utf-8

# split -l 8 hightemp.txt out

ht_list = open("hightemp.txt", encoding='utf-8').readlines()
print("n = ", end=' ')
n = int(input()) #n = 3
line_num = len(ht_list) // n
for i in range(n):
	f = open("out" + str(i) + ".txt", "w", encoding='utf-8')
	for line in ht_list[line_num * i:line_num * (i + 1)]:
		f.write(line)

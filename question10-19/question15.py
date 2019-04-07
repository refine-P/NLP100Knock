#coding:utf-8

# tail -n 5 hightemp.txt

print("n=", end=' ')
n = int(input())

hightemp_list = open("hightemp.txt", encoding='utf-8').readlines()[-n:]

for i in range(n):
	print(hightemp_list[i], end=' ')

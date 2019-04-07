#coding:utf-8

# head -n 5 hightemp.txt

hightemp_list = open("hightemp.txt", encoding='utf-8').readlines()

print("n=", end=' ')
n = int(input())

for i in range(n):
	print(hightemp_list[i], end=' ')
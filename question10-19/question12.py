#coding:utf-8

# cut -f 1 hightemp.txt
# cut -f 2 hightemp.txt

f1 = open("col1.txt", 'w', encoding='utf-8')
f2 = open("col2.txt", 'w', encoding='utf-8')

for line in open("hightemp.txt", encoding='utf-8'):
	line_list = line.split()
	f1.write(line_list[0] + '\n')
	f2.write(line_list[1] + '\n')
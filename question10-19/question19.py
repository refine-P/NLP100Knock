#coding:utf-8

# cut -f 1 hightemp.txt | sort | uniq -c | sort -k1nr

cnt_dict = {}
for line in open("hightemp.txt", encoding='utf-8'):
	factor = line.split()[0]
	if factor in cnt_dict:
		cnt_dict[factor] += 1
	else: 
		cnt_dict[factor] = 1

cnt_list = list(cnt_dict.items())

cnt_list.sort(key=lambda factor: factor[1], reverse=True)
for factor in cnt_list:
	print(factor[0], factor[1])
#coding:utf-8

import json

data = {}
cnt = 0
for line in open("jawiki-country.json", encoding='utf-8'):
	tmp = json.loads(line)
	data[tmp['title']] = tmp['text']

with open('uk.txt', 'w', encoding='utf-8') as f:
	f.write(data['イギリス'] + '\n')
	
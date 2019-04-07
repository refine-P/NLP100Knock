#coding:utf-8

import re

pattern = r"(={2,})(.+?)={2,}"
repatter = re.compile(pattern)
for line in open("uk.txt", encoding='utf-8'):
	matchOB = repatter.match(line)
	if matchOB:
		print(matchOB.group(2), int(len(matchOB.group(1))) - 1)
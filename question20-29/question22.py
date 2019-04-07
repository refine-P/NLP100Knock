#coding:utf-8

import re

pattern = r"\[\[Category:(.+?)(\|.*)*\]\]"
repatter = re.compile(pattern)
for line in open("uk.txt", encoding='utf-8'):
	matchOB = repatter.match(line)
	if matchOB:
		print(matchOB.group(1))
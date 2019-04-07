#coding:utf-8

import re

pattern = r"\{\{基礎情報 国\n(.+?)\}\}\n"
repatter = re.compile(pattern, re.DOTALL)
str1 = open("uk.txt", encoding='utf-8').read()
matchOB = repatter.search(str1)

if matchOB:
	#print(matchOB.group(1))
	pattern2 = r"\|(.+?) = (.+?)(?:(?=\n\|)|(?=\n$))"
	repatter2 = re.compile(pattern2, re.MULTILINE + re.DOTALL)
	re_list = repatter2.findall(matchOB.group(1))

	template_dict = {}
	for factor in re_list:
		str2 = re.sub(r"\'{2,5}(.+?)\'{2,5}", r"\1", factor[1])
		matchOB2 = re.search(r"\[\[(.+?)\]\]", str2)
		if matchOB2 and (matchOB2.group(1).count('|') <= 1):
			str2 = re.sub(r"\[\[[;#]{0,1}(?:[^\]]+?\|){0,1}(.+?)\]\]", r"\1", str2)
		template_dict[factor[0]] = str2
		print(factor[0], str2)
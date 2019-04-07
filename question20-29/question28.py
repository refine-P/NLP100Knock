#coding:utf-8

import re

#25. テンプレートの抽出
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
		#26. 強調マークアップの除去
		str2 = re.sub(r"\'{2,5}(.+?)\'{2,5}", r"\1", factor[1])

		#27. 内部リンクの除去(+ファイルの除去)
		matchOB2 = re.search(r"\[\[(.+?)\]\]", str2)
		if matchOB2:# and (matchOB2.group(1).count('|') <= 1):
			str2 = re.sub(r"\[\[[;#]{0,1}(?:[^\]]+?\|)*(.+?)\]\]", r"\1", str2)

		#<br>タグの処理
		str2 = re.sub(r"<br\s*/>", "\n", str2)

		#<ref>タグの除去
		str2 = re.sub(r"</*?ref.*?>", "", str2)

		#Template:Langの除去
		str2 = re.sub(r"\{\{.+?\|.+?\|(.+?)\}\}", r"\1", str2)

		#外部リンクの除去
		str2 = re.sub(r"\[.+? (.+?)\]", r"\1", str2)

		#箇条書きの処理
		str2 = re.sub(r"\*(?=\*)", "\t" , str2, re.MULTILINE)
		str2 = re.sub(r"\*", "・", str2, re.MULTILINE)

		template_dict[factor[0]] = str2
		print(factor[0], str2)

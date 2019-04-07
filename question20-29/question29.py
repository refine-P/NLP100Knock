#coding:utf-8

import re
from urllib.parse import urlparse
import urllib.request

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
		str2 = re.sub(r"<br\s*/>", "\n", str2)
		template_dict[factor[0]] = str2

url = "https://ja.wikipedia.org/w/api.php?action=query&titles=ファイル:%s&format=json&prop=imageinfo&iiprop=url" % (template_dict['国旗画像'])

#urlの文字列に日本語が含まれてると死ぬ
#参考(http://qiita.com/mix/items/87d094414e46f857de45#%E8%BF%BD%E8%A8%98%E4%BB%8A%E5%9B%9E%E3%81%AE%E5%AF%BE%E5%BF%9C%E3%81%A7%E3%82%82%E3%81%A3%E3%81%A8%E3%82%82%E6%AD%A3%E3%81%97%E3%81%84%E6%96%B9%E6%B3%95)
p = urlparse(url)
query = urllib.parse.quote_plus(p.query, safe='=&')
url = '{}://{}{}{}{}{}{}{}{}'.format(
    p.scheme, p.netloc, p.path,
    ';' if p.params else '', p.params,
    '?' if p.query else '', query,
    '#' if p.fragment else '', p.fragment)
response = urllib.request.urlopen(url)

print(eval(response.read())['query']['pages']['-1']['imageinfo'][0]['url'])

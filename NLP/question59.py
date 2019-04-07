#coding:utf-8

import xml.etree.ElementTree as ET
import re
import pyparsing as pp

def changeParseListToString(parse_list):

	res = ""
	for nex in parse_list[1:]:
		if len(res) != 0:
			res += " "

		if type(nex) == list:
			res += changeParseListToString(nex)
		else:
			res += nex
	
	return res

def searchNounPhrase(parse_list):

	res = []
	for nex in parse_list[1:]:
		if type(nex) != list:
			continue

		res.extend(searchNounPhrase(nex))

	if parse_list[0] == "NP":
		res.append(changeParseListToString(parse_list))

	return res


if __name__ == "__main__":
	tree = ET.parse('nlp.txt.xml')
	root = tree.getroot()

	for par in root.iter('parse'):
		parse_text = re.sub(r"\s+", " ", par.text)
		parse_text = parse_text.strip()

		#pyparsingのparse結果をlistに変換(pyparsing.ParseResults -> list)
		parse_list = eval(str(pp.nestedExpr().parseString(parse_text)))[0]

		print("\n".join(searchNounPhrase(parse_list)))
		print("")

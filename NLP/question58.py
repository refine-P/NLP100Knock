#coding:utf-8

import xml.etree.ElementTree as ET


if __name__ == "__main__":

	tree = ET.parse('nlp.txt.xml')
	root = tree.getroot()

	for dependencies in root.iter("dependencies"):

		if dependencies.get('type') != "collapsed-dependencies":
			continue

		dep_dict = {} #key=術語のidx, value=[術語, 主語のリスト, 目的語のリスト]

		#係り受け解析の結果（collapsed-dependencies）の読み込み
		for dep in dependencies.iter('dep'):

			g = dep.find('governor')
			d = dep.find('dependent')

			#主語の場合
			if dep.get('type') == 'nsubj':

				if int(g.get('idx')) not in dep_dict:
					dep_dict[int(g.get('idx'))] = [g.text, [], []]

				dep_dict[int(g.get('idx'))][1].append(d.text)

			#目的語の場合
			elif dep.get('type') == 'dobj':

				if int(g.get('idx')) not in dep_dict:
					dep_dict[int(g.get('idx'))] = [g.text, [], []]

				dep_dict[int(g.get('idx'))][2].append(d.text)			

		#「主語 述語 目的語」の組をタブ区切り形式で出力
		for key in sorted(dep_dict.keys()):
			pred = dep_dict[key][0]

			for nsubj in dep_dict[key][1]:
				for dobj in dep_dict[key][2]:
					print("\t".join([nsubj, pred, dobj]))
					
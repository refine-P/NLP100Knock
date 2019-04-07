#coding:utf-8

import xml.etree.ElementTree as ET
from graphviz import Digraph
import sys


if __name__ == "__main__":
	tree = ET.parse('nlp.txt.xml')
	root = tree.getroot()

	print("係り受けしたい文章のidを入力してください:", end=' ')
	sys.stdout.flush()
	target_id = int(input())

	graph = Digraph(filename='output', format='png')
	current_id = 0
	for dependencies in root.iter("dependencies"):

		if dependencies.get('type') != "collapsed-dependencies":
			continue

		current_id += 1
		if target_id != current_id:
			continue

		for dep in dependencies.iter('dep'):

			if dep.get('type') == 'punct':
				continue

			g = dep.find('governor')
			d = dep.find('dependent')

			graph.node(g.get('idx'), label=g.text)
			graph.node(d.get('idx'), label=d.text)

			graph.edge(g.get('idx'), d.get('idx'))

		graph.view(cleanup=True)
		break
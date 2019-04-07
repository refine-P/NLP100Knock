#coding:utf-8

import os
import subprocess
from question41 import inputCabocha
from graphviz import Digraph

def drawTree(chunks):
	graph = Digraph(filename='output', strict=True, encoding='UTF-8', format='png')
	graph.node_attr["fontname"] = "MS UI Gothic"
	for src in range(len(chunks)):
		dst = chunks[src].dst
		if dst == -1:
			continue
		src_label = chunks[src].getChunkSurface()
		dst_label = chunks[dst].getChunkSurface()
		if src_label == "" or dst_label == "":
			continue
		graph.node(str(src), label=src_label)
		graph.node(str(dst), label=dst_label)
		graph.edge(str(src), str(dst))

	graph.view(cleanup=True) 
	#print(graph.pipe('dot'))

if __name__ == "__main__":
	sentence = input()
	with open("tmp.txt", "w", encoding='utf-8') as f:
		f.write(sentence)

	cmd = "cabocha -f1 tmp.txt -o tmp.txt.cabocha"
	subprocess.call(cmd.split())

	neko_list = inputCabocha("tmp.txt.cabocha")
	drawTree(neko_list[0])

	os.remove("tmp.txt")
	os.remove("tmp.txt.cabocha")

#coding:utf-8

from question41 import inputCabocha
import pygraphviz as pgv

def drawTree(chunks):
	graph = pgv.AGraph(directed=True, encoding='UTF-8')
	graph.node_attr['fontname'] = 'MS UI Gothic'
	for src in xrange(len(chunks)):
		dst = chunks[src].dst
		if dst == -1:
			continue
		src_label = chunks[src].getChunkSurface()
		dst_label = chunks[dst].getChunkSurface()
		if src_label == "" or dst_label == "":
			continue
		graph.add_node(src, label=src_label.decode('UTF-8'))
		graph.add_node(dst, label=dst_label.decode('UTF-8'))
		graph.add_edge(src, dst)

	#print graph
	graph.layout('dot')
	graph.draw('output2.png')

if __name__ == "__main__":
	neko_list = inputCabocha()
	drawTree(neko_list[7])
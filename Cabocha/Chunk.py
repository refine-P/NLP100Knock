#coding:utf-8

class Chunk:

	def __init__(self, idx):
		self.idx = idx
		self.morphs = []
		self.dst = -1
		self.srcs = []

	def __str__(self):
		return ''.join(map(lambda m:m.surface, self.morphs)) + " " + str(self.srcs) + " " + str(self.dst)

	def getChunkSurface(self):
		res = ""
		for morpheme in self.morphs:
			if morpheme.pos != "記号":
				res += morpheme.surface
		return res

	def hasPos(self, pos):
		for morpheme in self.morphs:
			if morpheme.pos == pos:
				return True
		return False
		
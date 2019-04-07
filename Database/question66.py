#coding:utf-8

import json
import sys
from pymongo import MongoClient


if __name__ == "__main__":

	client = MongoClient()
	db = client['MusicBrainz']
	collection = db['artist']
	
	cnt = collection.count({'area' : 'Japan'})
	print("活動場所が「Japan」となっているアーティストの数は%d人です" % cnt)

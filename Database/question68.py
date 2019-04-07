#coding:utf-8

import codecs
import json
import sys
from pymongo import MongoClient, DESCENDING


if __name__ == "__main__":

	client = MongoClient()
	db = client['MusicBrainz']
	collection = db['artist']

	print("レーティングの投票数が多いダンスアーティスト・トップ10")
	for artist in collection.find({"tags.value": "dance"}).sort("rating.count", DESCENDING)[:10]:

		print("%s(id:%d)\t%d票" % (artist['name'], artist['id'], artist['rating']['count']))
		
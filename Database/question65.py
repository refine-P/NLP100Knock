#coding:utf-8

import codecs
import json
import sys
from pymongo import MongoClient


if __name__ == "__main__":

	client = MongoClient()
	db = client['MusicBrainz']
	collection = db['artist']

	for artist in collection.find({"name":"Queen"}):

		#ObjectIdの出力のための処理
		artist['_id'] = str(artist['_id'])

		#json文字列の整形
		#http://www.yoheim.net/blog.php?q=20150901
		print(json.dumps(artist, indent=2, ensure_ascii=False, sort_keys=True))
		print("")
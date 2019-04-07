#coding:utf-8

import json
import sys
from pymongo import MongoClient, ASCENDING


def buildMongoDB(collection, json_path='artist.json'):

	#初期化
	collection.drop()

	#jsonファイルの読み込み
	with open(json_path, 'r', encoding='utf-8') as f:

		buff = []
		cnt = 0
		for line in f:

			json_dict = json.loads(line)
			buff.append(json_dict)

			#1000件ごとにまとめて格納
			if len(buff) == 1000:
				collection.insert_many(buff)
				buff = []
				cnt += 1

				#10000件ごとに途中経過を表示
				if cnt % 10 == 0:
					print("complete %d" % (cnt * 1000))
					sys.stdout.flush()

		#残ったやつを格納
		if len(buff) > 0:
			collection.insert_many(buff)
		
		print("complete all")
		sys.stdout.flush()

	collection.create_index([('name', ASCENDING)])
	collection.create_index([('aliases.name', ASCENDING)])
	collection.create_index([('tags.value', ASCENDING)])
	collection.create_index([('rating.value', ASCENDING)]) #なくても問題なさそう
	collection.create_index([('area', ASCENDING)]) #あると後々役に立つ
	print("finish")



if __name__ == "__main__":

	client = MongoClient()
	db = client['MusicBrainz']
	collection = db['artist']

	buildMongoDB(collection)
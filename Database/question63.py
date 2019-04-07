#coding:utf-8

import sys
from redis import Redis
from question63_pre import buildKVSforTags

"""
正常に動作しない場合はquestion63_pre.pyを先に実行してください
(多分これだけ実行しても大丈夫なはず)
"""

if __name__ == "__main__":

	client = Redis(db=2)

	#DBが存在しない場合、新たに作成
	if client.dbsize() == 0:
		buildKVSforTags()

	print("アーティスト名を入力してください")
	sys.stdout.write("-> ") #改行なしの出力
	sys.stdout.flush()

	artist_name = input()

	for artist_id, artist_tags in sorted(list(client.hgetall(artist_name).items()), key=lambda d:int(d[0].decode('utf-8'))):

		#bytes型になってるので変換 
		artist_id = artist_id.decode('utf-8')
		artist_tags = artist_tags.decode('utf-8')

		print("%s(id:%s)のタグと被タグ数の一覧" % (artist_name, artist_id))

		#tagsをstrからlistに変換
		artist_tags = eval(artist_tags)

		for tag in artist_tags:
			print(tag['value'], tag['count'])
		print("")
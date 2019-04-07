#coding:utf-8

import json
from redis import Redis


def buildKVSforArea(json_path='artist.json'):

	#Redis serverの起動(1番のデータベースを使用)
	client = Redis(db=1)

	#データベースの初期化
	client.flushdb()

	#jsonファイルの読み込み
	with open(json_path, 'r', encoding='utf-8') as f:	
		for line in f:

			json_dict = json.loads(line)
			artist_name = json_dict['name']

			#同名のアーティストが複数いるのでidで区別する
			artist_id = json_dict['id']

			#活動場所が登録されていないアーティストがいるので、その場合は'UNKNOWN'とする
			artist_area = 'UNKNOWN'
			if 'area' in json_dict:
				artist_area = json_dict['area']

			#データベースの構造は下のような感じ
			#{'name1' : {'id1' : 'area1', 'id2' : 'area2', ...}, 'name2' : {...}, ...}
			client.hset(artist_name, artist_id, artist_area)  



if __name__ == "__main__":

	buildKVSforArea()
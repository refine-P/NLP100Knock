#coding:utf-8

import json
from redis import Redis


def buildKVSforTags(json_path='artist.json'):

	#Redis serverの起動(2番のデータベースを使用)
	client = Redis(db=2)

	#データベースの初期化
	client.flushdb()

	#jsonファイルの読み込み
	with open(json_path, 'r', encoding='utf-8') as f:	

		for line in f:

			json_dict = json.loads(line)

			artist_name = json_dict['name'].encode('utf-8')

			#同名のアーティストが複数いるのでidで区別する
			artist_id = json_dict['id']

			#タグが登録されていないアーティストがいるので、その場合はNo tagsと表示されるようにする
			artist_tags = [{'count' : 'tags', 'value' : 'No'}]
			if 'tags' in json_dict:
				artist_tags = json_dict['tags'] 

			#データベースの構造は下のような感じ
			#{'name1' : {'id1' : 'tags1', 'id2' : 'tags2', ...}, 'name2' : {...}, ...}
			client.hset(artist_name, artist_id, artist_tags)



if __name__ == "__main__":

	buildKVSforTags()
#coding:utf-8

import sys
from redis import Redis


if __name__ == "__main__":

	client = Redis(db=1)

	print("アーティスト名を入力してください")
	sys.stdout.write("-> ") #改行なしの出力
	sys.stdout.flush()

	artist_name = input()

	for artist_id, artist_area in sorted(list(client.hgetall(artist_name).items()), key=lambda d:int(d[0].decode('utf-8'))):

		#bytes型になってるので変換
		artist_id = artist_id.decode('utf-8')
		artist_area = artist_area.decode('utf-8') 
		
		print("%s(id:%s)の活動場所: %s" % (artist_name, artist_id, artist_area))
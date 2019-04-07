#coding:utf-8

from redis import Redis


def countArtistsInArea(area="Japan"):

	client = Redis(db=1)
	res = 0

	area = area.encode('utf-8') #bytes型にしておかないとダメ

	for key in list(client.keys()):
		res += len([a for a in client.hvals(key) if a == area])

	return res



if __name__ == "__main__":

	print(countArtistsInArea())
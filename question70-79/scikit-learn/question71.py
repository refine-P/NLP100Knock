#coding:utf-8

"""
ストップリスト(これを使うかは要検討)
参考(http://kenichia.hatenablog.com/entry/2016/02/22/111027)
出現頻度の高い上位100単語を抽出
その中でストップワードにするとまずそうなものを独断で除外(notなどの否定の意味を持つものはなるべく除外)
※これで大丈夫かどうかは適宜確認すべし

その他候補(既存のストップリストはnotとかの否定の意味を持つ単語が含まれているため極性分析には適さない?)
https://docs.oracle.com/cd/B28359_01/text.111/b28304/astopsup.htm#CCREF2295
http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/English.txt

Natural Language Toolkit(http://www.nltk.org/)のストップリストを使う
from nltk.corpus import stopwords
stoplist = stopwords.words("english")
"""

def makeStoplist(stoplist_file="stopwords.txt"):
	stoplist = []
	for line in open(stoplist_file, 'r', encoding='utf-8'):
		stoplist.append(line.rstrip())

	return stoplist


def isIncludedInStoplist(word, stoplist):
	return word in stoplist



if __name__ == "__main__":
	stoplist = makeStoplist()
	s = "i don't want to study English ."
	data = s.split()
	for word in data:
		print(word, isIncludedInStoplist(word, stoplist))
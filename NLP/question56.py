#coding:utf-8

import xml.etree.ElementTree as ET


#全文章をリスト化
def makeNLPList(root):

	res = []
	for tokens in root.iter('tokens'):
		sentence = []
		for token in tokens.iter('token'):
			sentence.append(token.findtext('word'))
		res.append(sentence)

	return res


if __name__ == "__main__":
	tree = ET.parse('nlp.txt.xml')
	root = tree.getroot()

	nlp_list = makeNLPList(root)

	#文章の置換部分を記憶するリスト
	repr_list = [[] for _ in range(len(nlp_list))] 

	#共参照解析の結果を読み込む
	for coref in root.iterfind('./document/coreference/coreference'):
		represent = None
		for ment in coref.iter('mention'):

			sentence_idx = int(ment.findtext('sentence')) - 1
			start_idx = int(ment.findtext('start')) - 1
			end_idx = int(ment.findtext('end')) - 1

			#代表参照表現の場合はそれを記憶する
			if ment.get('representative') == "true":

				represent = ment.findtext('text')
				#repr_list[sentence_idx].append((start_idx, "["))
				#repr_list[sentence_idx].append((end_idx, "]"))

			#そうでない場合は置換部分を記憶
			else:
				
				repr_list[sentence_idx].append((start_idx, "[ " + represent + " ] ("))
				repr_list[sentence_idx].append((end_idx, ")"))

	#文章の置換を行う(置換前と置換後の文章の差分を置換前の文章に挿入する形で行う)
	for idx in range(len(nlp_list)):

		#文中に参照表現がない場合(置換しない場合)
		if len(repr_list[idx]) == 0:
			print(" ".join(nlp_list[idx]))
			print("")
			continue

		#時系列順にソート
		repr_list[idx].sort(key=lambda x:x[0])
		
		#置換後の文章の作成
		text = " ".join(nlp_list[idx][:repr_list[idx][0][0]])
		
		for idx2 in range(len(repr_list[idx])):
			if text != "":
				text += " "

			text += repr_list[idx][idx2][1]

			if idx2 != len(repr_list[idx]) - 1:
				text += " " + " ".join(nlp_list[idx][repr_list[idx][idx2][0]:repr_list[idx][idx2 + 1][0]])
		
		text += " " + " ".join(nlp_list[idx][repr_list[idx][-1][0]:])			

		#置換後の文章の出力
		print(text)
		print("")
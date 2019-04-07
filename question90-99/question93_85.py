#coding:utf-8

from sklearn.metrics import accuracy_score

if __name__ == "__main__":

	y_true = []
	y_pred = []
	with open("analogy_result_family_85.txt", encoding='utf-8') as f:
		for line in f:
			result = line.split()
			y_true.append(result[3])
			y_pred.append(result[4])

	print(accuracy_score(y_true, y_pred))

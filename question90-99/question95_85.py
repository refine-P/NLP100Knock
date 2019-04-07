#coding:utf-8

from scipy.stats import spearmanr


if __name__ == "__main__":

	result_90 = None
	result_85 = None
	with open("combined.tab", encoding='utf-8') as fh, open("353_result_85.txt", encoding='utf-8') as f85:
		result_human = [float(line.split()[2]) for line in fh.readlines()[1:]]
		result_85 = [float(line.split()[2]) for line in f85]

	correlation, pvalue = spearmanr(result_human, result_85)
	print("correlation: " + str(correlation))
	print("pvalue: " + str(pvalue))

#coding:utf-8

from scipy.stats import spearmanr


if __name__ == "__main__":

	result_90 = None
	result_85 = None
	with open("combined.tab", encoding='utf-8') as fh, open("353_result.txt", encoding='utf-8') as f90:
		result_human = [float(line.split()[2]) for line in fh.readlines()[1:]]
		result_90 = [float(line.split()[2]) for line in f90]

	correlation, pvalue = spearmanr(result_human, result_90)
	print("correlation: " + str(correlation))
	print("pvalue: " + str(pvalue))

#coding:utf-8

def n_gram(sequence, n):
	s_len = len(sequence)
	if s_len < n:
		return sequence
	else:
		ans_list = []
		for i in range(s_len - n + 1):
			ans_list.append(sequence[i:i + n])
		return ans_list
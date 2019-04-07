#coding:utf-8

from ngram import n_gram

str1 = "paraparaparadise"
str2 = "paragraph"

str1_set = set(n_gram(str1, 2))
str2_set = set(n_gram(str2, 2))
print(list(str1_set))
print(list(str2_set))
print(list(str1_set & str2_set))
print(list(str1_set | str2_set))
print(list(str1_set - str2_set))
print("se" in str1_set)
print("se" in str2_set)
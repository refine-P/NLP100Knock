#coding:utf-8

import os.path
from shutil import copyfile
import subprocess
import sys

"""
参考
http://www.listofcountriesoftheworld.com/
http://kenichia.hatenablog.com/entry/2016/03/03/170718
http://linux.just4fun.biz/?%E9%80%86%E5%BC%95%E3%81%8DUNIX%E3%82%B3%E3%83%9E%E3%83%B3%E3%83%89/sed%E3%82%B3%E3%83%9E%E3%83%B3%E3%83%89%E3%81%A7%E5%A4%A7%E6%96%87%E5%AD%97%E5%B0%8F%E6%96%87%E5%AD%97%E3%82%92%E5%8C%BA%E5%88%A5%E3%81%9B%E3%81%9A%E3%81%AB%E7%BD%AE%E6%8F%9B%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95
"""

if __name__ == "__main__":

	if not os.path.isfile("tokens_r100.txt"):
		sys.exit("You should make 'tokens.txt' by question80.py")

	copyfile("tokens_r100.txt", "tokens2_r100.txt")

	with open("country_list.txt") as fc:
		for country in fc:
			country = country.rstrip()
			cmd = ['sed','-i','-e']
			pattern = "s/%s/%s/g" % (country, "_".join(country.split()))
			cmd.append(pattern)
			cmd.append("tokens2_r100.txt")
			subprocess.call(cmd)

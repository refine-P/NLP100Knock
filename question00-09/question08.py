#coding:utf-8

def cipher(s):
	str_list = list(s)
	for i in range(len(str_list)):
		if str_list[i].islower():
			str_list[i] = chr(219 - ord(str_list[i]))
	return "".join(str_list)

print("s=", end=' ')
s = input()
enc = cipher(s)
print(enc)
dec = cipher(enc)
print(dec)
#coding:utf-8

def templateString(x, y, z):
	return "%s時の%sは%s" % (x, y, z)

print("x=", end=' ')
x = input()
print("y=", end=' ')
y = input()
print("z=", end=' ')
z = input()

print(templateString(x, y, z))
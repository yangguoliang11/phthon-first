# -*- coding: utf-8 -*-

L = ["tom","kite","lucy","mama"]
print L[0:3]

print L[:]

print L[::3]

print L[1::2]



print L[-2:4]


s = "abcdefg"

print s[0:4]

print s[-3:7]


print s.upper()

print range(1,101)


for index,item in enumerate(L):
	print index,'-',item


d = {"Adam":12,"Pipe":16,"Lucy":99}

for name in d.values():
	print name

for name in d.itervalues():
	print name

for key,name in d.items():
	print key,'-',name

for key,name in d.iteritems():
	print key,'-',name


print range(1,100)

L = []
for item in range(1,11):
	L.append(item*item)

print L

L = [x*x for x in range(1,11)]

print L
# -*- coding: utf-8 -*-
age = 20
if age==20:
#缩进请严格按照Python的习惯写法：4个空格，不要使用Tab，更不要混合Tab和空格
	print "your age is",age
	print 'adult'
print 'END'



age = 8
if age>10:
	print "your age is:",age
else:
	print "below 10:",age
print "============="
print 9==9.0
print "============="

age = 9.0;
if age >8:
	print "your age:",age
else:
	if age<10:
		print "babababab"
	else:
		print "ccccccccccccc"

if age > 8:
	print "your age:",age
elif age<10:
	print "your age:",age,"<10"
elif age==9:
	print "999999999999999999999999",age
else:
	print u"什么鬼啊"


L = [1,2,3,4,5]

for name in L:
	print name

L = ("a","b",True,None,None)
for name in L:
	print name


age = 0
sum = 0
man = 13

while age < man:
	age = age +1
	sum = sum + age
	if(age ==10):
		break
print sum

for x in ["a","b","c"]:
	for y in ["1","2","3"]:
		print x+y



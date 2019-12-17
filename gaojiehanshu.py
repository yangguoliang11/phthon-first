# -*- coding: utf-8 -*-
f=abs
def add(x,y,f):
	return f(x)+f(y)

print add(-5,9,f)


def sqrt(x,y,f):
	return f(x)+f(y)

import math
print sqrt(10,10,math.sqrt)

def f(x):
	return x*x

print map(f,[1,2,3,4,5,6,7]);


L = ['aDam','LISA','BarT']

def ff(x):
	return x[0].upper()+x[1:len(x)].lower()

print map(ff,L)

def ji(x,y):
	return x*y

#reduce()函数也是Python内置的一个高阶函数。reduce()函数接收的参数和 map()类似，一个函数 f，一个list，但行为和 map()不同，reduce()传入的函数 f 必须接收两个参数，reduce()对list的每个元素反复调用函数f，并返回最终结果值。
print reduce(ji,[1,2,3,4,5])

def is_odd(x):
	if(x%2==1):
		return True
	else:
		return False

print filter(is_odd,[1,2,3,4,4,5,6,7,8])

def is_not_empty(s):
	return s and len(s.strip()) > 0

print filter(is_not_empty,["1","2",'',"3","4","55",'',"555"])

#排序

num = [1,2,3,4,5,4,3,1,66,22,11,2,3,4]
print sorted(num)

#烦着排序

def fan(x,y):
	if(x>y):
		return -1
	elif(x<y):
		return 1
	else:
		return 0

print sorted(num,fan)


def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0
print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)

def cal(x,y):
	return x*y
def calc_prod(list1):
	def call():
		return reduce(cal,list1,1)
	return call

#像这种内层函数引用了外层函数的变量（参数也算变量），然后返回内层函数的情况，称为闭包（Closure）。

f = calc_prod([1,2,3,4]);

print f

#内置函数延迟调用
print f()

#匿名函数
print map(lambda x:x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])



print sorted([1,2,3,4,7,12,3,4],lambda x,y:-cmp(x,y))


print filter(lambda x:len(x.strip())>0,["test","","","TT"])




#装饰器

def f1(x):
	return x*2

def f2(x):
	return x+2

def f3(x):
	return x/2

def new_fn(f):
	def fn(x):
		print 'call'+f.__name__+'()'
		return f(x)
	return fn


now_f1 = new_fn(f1)
print now_f1
print now_f1(3)


now_f2 = new_fn(f2)
print now_f2
print now_f2(3)

now_f3 = new_fn(f3)
print now_f3
print now_f3(3)

@new_fn
def f4(x):
	return x*2

@new_fn
def f5(x):
	return x+2

@new_fn
def f6(x):
	return x/2

print f6(3)
print f5(3)
print f4(3)

























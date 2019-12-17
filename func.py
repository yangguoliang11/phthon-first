# -*- coding: utf-8 -*-
def my_abs(x):
	if x>=0:
		return x
	else:
		return -x

print my_abs(-100)


import math

def move(x,y,step,angle):
	nx = x + step * math.cos(angle)
	ny = y + step * math.sin(angle)
	return nx,ny

x,y = move(100,100,60,math.pi/6)

print x,y

def average(*args):
	key = 0
	sum2 = 0
	for item in args:
		key = key+1
		sum2 = sum2+item

	return 0

def average(*args):
	lens = len(args)
	sum2 = sum(args)

	return sum2/lens

print average(1,2,3)

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
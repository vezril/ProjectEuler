#!/usr/bin/env python
import math

def pythagor(a,b):
	return math.sqrt((a*a) + (b*b))
	
target = 1001

for a in range(0,target):
	for b in range(0,target):
		c = pythagor(a,b)
		if (a+b+c) == 1000:
			if (a < b) and (b < c):
				print "A: " + str(a)
				print "B: " + str(b)
				print "C: " + str(c)
				print a*b*c
				break
			
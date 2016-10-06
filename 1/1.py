#!/usr/bin/env python

rez = 0
for n in range(1,1000):
	if (n % 3 == 0) or (n % 5 == 0):
		rez += n

print "Answer is: " + str(rez)
#!/usr/bin/env python

num1 = 1
num2 = 1
rez = 0

while True:
#for n in range(0,10):
	temp = num1 + num2
	if temp > 4000000:
		break
#	print temp,
	
	if temp % 2 == 0:
		rez += temp
	num1 = num2
	num2 = temp
	
print "Answer is: " + str(rez)
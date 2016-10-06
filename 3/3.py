#!/usr/bin/env python
import math

num = 600851475143
n = num/2

#n = math.ceil(math.sqrt(600851475143))
#n = int(n)

print n

while True:
	if num % n == 0:
		print "Answer: " + str(n)
		break
	n = n-1
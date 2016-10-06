#!/usr/bin/env python

def collatz(n):
	if n%2 == 0: return n/2
	else: return (3*n)+1
	
def collatz_2(n,m=1):
	if n == 1:
		return m
	elif n%2 == 0:
		x = collatz_2(n/2,m+1)
	else:
		x = collatz_2((3*n)+1,m+1)
	return x

#print collatz_2(999999)
#raw_input()
save = 0

for n in range(1,1000000):
	#print "Trying with N=" + str(n)
	val = collatz_2(n)
	if val > save:
		#print "Trigged on: " + str(n)
		save = val
		big = n
print "Biggest chain was with N=" +str(big) + "!"
	
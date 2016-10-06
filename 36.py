#!/usr/bin/env python

def is_palindrome(n):
	head = str(n)
	tail = head[::-1]
	
	if tail == head:
		return True
	else:
		return False
		
#print is_palindrome(10101)
LIMIT = 1000000
sum = 0
for n in range(0,LIMIT):
	if is_palindrome(n):
		if is_palindrome(bin(n)[2:]):
			sum = sum + n
print sum
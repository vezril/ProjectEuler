#!/usr/bin/env python
from sys import exit

def is_triangle(n):
	if n == 1:
		return True
	tri = 1
	m = 1
	cnt = 1
	while(tri < n):
		tri = 0.5 * cnt * (cnt+1)
		if(tri == n):
			return True
		cnt = cnt + 1
	return False

try:
	f = open('words.txt','r')
except:
	print "Unable to open file..."
	exit(1)
	
lookup_t = {}
cnt = 1
for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
	lookup_t[char] = cnt
	cnt = cnt + 1

data = f.readlines()
data = data[0]
data = data.split(',')
cnt = 0

for words in data:
	sum = 0
	word = words.strip('"')
	for char in word:
		sum = sum + lookup_t[char]
		
	if is_triangle(sum):
		cnt = cnt + 1
		
print cnt
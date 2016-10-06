#!/usr/bin/env python
from sys import exit
'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical 
position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
So, COLIN would obtain a score of 938  53 = 49714.

What is the total of all the name scores in the file?
'''

try:
	f = open('names.txt','r')
except:
	print 'Unable to open names.txt'
	exit(1)
	
data = f.readlines()
data = data[0]
f.close()

data = data.split(',')
names = []
for name in data:
	names.append(name[1:-1])
	
names.sort()
#64
sum = 0
cnt = 0
for name in names:
	cnt = cnt + 1
	c_sum = 0
	for c in name:
		c_sum = c_sum + (ord(c) - 64)
	print '[DEBUG], CNT: ' + str(cnt) + ' c_sum:' + str(c_sum)
	sum = sum + (c_sum * cnt)
	
print sum
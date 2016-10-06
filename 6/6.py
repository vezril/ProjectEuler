#!/usr/bin/env python

sum_os = 0
square_os = 0
for n in range(1,101):
	sum_os += n*n
	
for n in range(1,101):
	square_os += n
square_os *= square_os
print(square_os-sum_os)
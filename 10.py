#!/usr/bin/env python

f = open('primes.csv', 'r')

sum = 0

while True:
    try:
        n = int(((f.readline()).split(','))[1])
        if n < 2000000: sum = sum + n
        else: break
    except:
        break
print sum
        
        
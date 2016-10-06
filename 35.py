#!/usr/bin/env python

f = open('primes.csv', 'r')

def circulate(n):
    if n < 10: return [n]
    
    num = str(n)
    for i in range(0,len(num)):
        
       
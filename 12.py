#!/usr/bin/env python

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def get_factors(value):
    d = []      
    for n in range(0,value+1):
        tmp = gcd(value,n)
        try:
            d.index(tmp)
        except ValueError:
            d.append(tmp)
    d.sort()
    return d
    
n = 1
m = 1
while True:
    d = get_factors(n)
    if len(d) >= 500:
        break
    m = m +1
    n = n+m
print n
print d
#!/usr/bin/env python
'''
http://en.wikipedia.org/wiki/Divisors

n=p1^v1 p2^v2 ... pn^vn     <---- List of prime divisors
d(n) = (v1+1)(v2+1)...(vn+1)

'''
from math import sqrt, ceil

        
def factor(n):
    return factor_fermat(n)

def factor_fermat(n):
    a = ceil(sqrt(n))
    b2 = a*a - n

    while (sqrt(b2) - int(sqrt(b2)) != 0):
        a = a+1
        b2 = a*a - n

    if int(a-sqrt(b2)) == 1:
        return []
    else:
        return [int(a+sqrt(b2)),int(a-sqrt(b2))]  
        
n = 7
m = 0
triangle = 0

print factor(int(raw_input()))

# factors = [(1,[1]), (2,[2,1]), (3,[3,1]), (4,[4,2]), (5,[5,1]), (6,[6,3,2,1]) ]
# Generate Triangle numbers:
# while True:
    # triangle = triangle + m
    
    # print factor(14)
    
    # if m == 7:
        # break
        
        
    #Next iteration    
    # m = m+1
	
print m
print triangle
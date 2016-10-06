#!/usr/bin/env python

from fractions import gcd
from sys import exit
def g(n,i,j,k,l,recur=0):
    try:
        recur += 1
    except:
        recur = None

    if recur != None:
        print 'Recursicve depth: ' + str(recur)

    if n == 0:
        return i
    elif n == 1:
        return j
    elif n == 2:
        return k
    elif n == 3:
        return l
    elif n == 4:
        return 13
    else:
        return g(n-1,i,j,k,l,recur) + gcd(n,g(n-1,i,j,k,l, None))
        
if __name__ == "__main__":
    
    lookup = {4:13, 5:14, 6:16, 7:17, 8:18, 9:27, 10:28, 11:29, 12:30, 13:31, 14:32, 15:33, 16:34, 17:51, 18:54, 19:55, 20:60}
    
    for i in range(0,13):
        for j in range(0,13):
            for k in range(0,13):
                for l in range(0,13):
                    for n in range(4,21):
                        x = g(n,i,j,k,l)
                        
                        if lookup[n] != x:
                            pass
                            
                        if n == 20 and x == 60:
                        # g(1 000) = 2524 and g(1 000 000) = 2624152.
                            if g(1000,i,j,k,l) == 2524:
                                if g(1000000,i,j,k,l) == 2624152:
                                    print 'found'
                                    print i,j,k,l
                                    exit(1)
                            
    

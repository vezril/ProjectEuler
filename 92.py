#!/usr/bin/env python

def number_chain(n):
    sum = 0
    m = str(n)
    for i in range(0,len(m)):
        sum = sum + ((int(m[i])) * (int(m[i])))
    if sum == 89:
        return 1
    elif sum == 1 or sum == 0:
        return 0
    else:
        x = number_chain(sum)
    return x

def number_chain2(n):
    sum = 0
    m = str(n)
    for i in range(0,len(m)):
        sum = sum + ((int(m[i])) * (int(m[i])))
    return sum
        
# print number_chain(145) 
# raw_input()
    
MAX = 10000000   
counter = 0
for n in range(1,MAX):
    if number_chain(n) == 1:
        counter = counter + 1
print counter
        
# for n in range(1,MAX):
    # while True:
        
#!/usr/bin/env python

f = open('matrix.txt','r')

data = f.readlines()
matrix = []
f.close()

for n in range(0,len(data)):
    matrix.append(((data[n].rstrip()).split(',')))
    
i = 0
j = 0
sum = 0

while True:
    sum = sum + int(matrix[i][j])
    if (i >= 79) and (j >= 79): break
    if i == 79: j = j + 1
    elif j == 79: i = i + 1 
    elif int(matrix[i+1][j]) > int(matrix[i][j+1]): i = i + 1
    elif int(matrix[i+1][j]) < int(matrix[i][j+1]): j = j + 1
    else: 
        print "Oops..."
        break
print i,j
print sum
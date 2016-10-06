#!/usr/bin/env python
import sys
num = 1

while True:
    for n in range(1,21):
		
        if num % n != 0:
            break
        if n == 20:
            print(num)
            sys.exit(0)
    num += 1
#!/usr/bin/env python

digit1 = 999
digit2 = 999
mul = 0
largest = 0

while digit1 != 0:
	while digit2 != 0:
		mul = digit1*digit2
		save = mul
		# 987 789
		d1_1 = mul % 10
		mul /= 10
		d1_2 = mul % 10
		mul /= 10
		d1_3 = mul % 10
		mul /= 10
		
		d2_3 = mul % 10
		mul /= 10
		d2_2 = mul % 10
		mul /= 10
		d2_1 = mul % 10
		if d1_1 == d2_1:
			if d1_2 == d2_2:
				if d1_3 == d2_3:
					if save > largest:
						largest = save
		if digit2 == 100:
			digit2 = 999
			break
		digit2 = digit2 - 1
		
	digit1 = digit1 - 1
print 'Answer is: ' + str(largest)
#!/usr/bin/env python

def int2word(n):
    ones = ['zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine']

    tens = ['ten',
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen']

    twenties = ['ten',
    'ten',
    'twenty',
    'thirty',
    'fourty',
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety']

    word = ''
    
    b1 = (n/1000) % 10
    b2 = (n/100) % 10
    b3 = (n/10) % 10
    b4 = n % 10
    
    if b1 > 0:
        word = ones[b1] + ' thousand'
        if b2 == 0:
            if b3 != 0:
                word = word + ' and'
            
    
    if b2 > 0:
        word = word + ' ' +ones[b2] + ' hundred'
        if b3 > 0 or b4>0:
           # if b4 > 0:
            word = word + ' and'
                
    if b3 == 1:
        word = word + ' ' + tens[b4]
    if b3 > 1:
        word = word + ' ' + twenties[b3]
        if b4>0:
             word = word + ' ' + ones[b4]
    else:
   #s     print "[DEBUG]"
        if b3 !=1:
            if b4 != 0:
                word = word + ' ' + ones[b4]
        
    return word.lstrip()
    
#print int2word(int(raw_input()))
sum = 0
for n in range(1,1001):
    print int2word(n)
    sum = sum + len((str(int2word(n))).replace(' ',''))
    
print sum
    
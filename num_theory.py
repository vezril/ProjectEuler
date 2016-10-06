from math import sqrt, ceil

#########################################################################
# Factorisation
#########################################################################

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
        

# GCD

def gcd(a, b):
    return gcd_euclid(a,b)

def gcd_euclid(a, b):
    if b == 0:
        return a
    else:
        return gcd_euclid(b, a % b)

########################## PRIME FUNTIONS ###################################
# Prime Generation
#########################################################################

def sieve(n):
    return sieve_eratosthenes(n)

def sieve_eratosthenes(n):

    sieve = [2]

    if n < 2:
        return []

    # Generate list, start by removing 2
    for p in range(3,n):
        if is_even(p):
            continue
        else:
            sieve.append(p)

    # Lets being this shit!
    p = 3
    i = 2
    while p<sqrt(n):
        while(i*p<n):
            try:
                sieve.remove(i*p)
                i = i+1
            except:
                i = i+1
                continue
        p = p+1
        i = 2

    return sieve

#########################################################################
# Prime Test
#########################################################################

def is_prime(n):
    return is_prime_brute(n)

def is_prime_brute(n):
    if(n == 2):
        return 1
    for i in range(2,sqrt(n))
        if n%i == 0:
            return 0
    return 1
    
def is_prime_miller_rabin(n,k):
    return 0

#########################################################################
# Prime Find
#########################################################################

def find_prime(n):
    data = sieve(int((n*n)))
    return data[n]

def algo_1(n):

    sieve = [2]

    if n < 2:
        return []

    # Generate list, start by removing 2
    for p in range(3,n*n):
        if is_even(p):
            continue
        else:
            sieve.append(p)

    # Lets being this shit!
    p = 3
    i = 2
    while p<sqrt(n):
        while(i*p<n):
            try:
                sieve.remove(i*p)
                i = i+1
            except:
                i = i+1
                continue
        p = p+1
        i = 2

    return sieve


#########################################################################
# Random stuff
#########################################################################

def is_odd(n):
    if n % 2 == 0:
        return False
    else:
        return True

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

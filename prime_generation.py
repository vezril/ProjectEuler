#!/usr/bin/env python
from math import sqrt

def gen_prime(lim):

    sqrtlim=sqrt(float(lim))
    pp=2
    ss=[pp]
    ep=[pp]
    pp+=1
    rss=[ss[0]]
    tp=[pp]
    i=0
    rss.append(rss[i]*tp[0])
    xp=[]
    pp+=ss[0]
    npp=pp
    tp.append(npp)
	
    while npp<int(lim):
            i+=1
            while npp<rss[i]+1:
                    for n in ss:
                            npp=pp+n
                            if npp>int(lim): break
                            if npp<=rss[i]+1: pp=npp
                            sqrtnpp=sqrt(npp)
                            test=True
                            for q in tp:
                                    if sqrtnpp<q: break
                                    elif npp%q==0:
                                            test=False
                                            break
                            if test:
                                    if npp<=sqrtlim: tp.append(npp)
                                    else: xp.append(npp)
                    if npp>int(lim): break
            if npp>int(lim): break
            lrpp=pp
            nss=[]
            while pp<(rss[i]+1)*2-1:
                    for n in ss:
                            npp=pp+n
                            if npp>int(lim): break
                            sqrtnpp=sqrt(npp)
                            test=True
                            for q in tp:
                                    if sqrtnpp<q: break
                                    elif npp%q==0:
                                            test=False
                                            break
                            if test:
                                    if npp<=sqrtlim: tp.append(npp)
                                    else: xp.append(npp)
                            if npp%tp[0]!=0:
                                    nss.append(npp-lrpp)
                                    lrpp=npp
                            pp=npp
                    if npp>int(lim): break
            if npp>int(lim): break
            ss=nss
            ep.append(tp[0])
            del tp[0]
            rss.append(rss[i]*tp[0])
            npp=lrpp
    ep.reverse()
    [tp.insert(0,a) for a in ep]
    tp.reverse()
    [xp.insert(0,a) for a in tp]
    return xp
    
if __name__ == "__main__":
    lim = raw_input("\nGenerate prime numbers up to what number? : ")
    xp = gen_prime(lim)
    f = open('primes_big.csv', 'w')
    for n in range(0,int(lim)):
        try:
            f.write(str(n+1) + "," + str(xp[n])+"\n")
        except IndexError:
            break    
    f.close()
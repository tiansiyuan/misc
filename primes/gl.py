#!/usr/bin/env python

def isprime(n):
    if n==2:return True
    if n<3 or (n%2 == 0):return False
    for i in range(3,n-1,2):
        if n%i==0:
            return False
    return True

def modexp(a,b,p):
    ret = 1
    t = a;
    while b!=0:
        if (b&1)==1:
            ret=ret*t%p
        b>>=1
        t=t*t%p
    return ret

def inv(n,p):
    return modexp(n,p-2,p);

def findinv(p):
    ret = [0] * p
    for i in range(1,p):
        ret[i]=inv(i,p)
    return ret

def isgood(p):
    iv = findinv(p)
    i = 1
    j = 1
    s = 0
    while i<p-1:
        j = j*i%p
        s = (s+iv[i])%p
        if (j * s % p) == 0:
            #print "!!%d" % i
            return True
        i+=1
    return False


def test():
    x=['isprime(2)==True',
       'isprime(3)==True',
       'isprime(5)==True',
       'isprime(4)==False',
       'isprime(19)==True',
       'isprime(18)==False',
       'isprime(2357)==True',
       'modexp(2,3,5)==3',
       'modexp(2,8,10)==6',
       'modexp(3,4,5)==1',
       'modexp(6,2,4)==0',
       'findinv(7)',
       'modexp(10,0,10)==1',
       'isgood(11)==True',
       'isgood(29)==True',
       'isgood(37)==True',
       'isgood(43)==True',
       'isgood(53)==True',
       'isgood(47)==False',
       'isgood(41)==False',
       'isgood(31)==False']
    for i in x:
        print i,eval(i)

if __name__ == '__main__':
    test()
    ret = filter(lambda i:isprime(i) and isgood(i),range(1,10000))
    #print ret
    with open('all_lt_10000.txt','w') as f:
        f.write(str(ret))
    print 'size of ret:',len(ret)

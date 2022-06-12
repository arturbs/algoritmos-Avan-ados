#errado, runtime error (nzec), provavelmente certa, mas não consegui consertar esse erro da entrada automática

import math
MOD = 1000000007
def md(m): return ((m % MOD) + MOD) % MOD

def invMod(a): return math.pow(a, MOD - 2, MOD)

fact = [1] * 1000001
invfact = [1] * 1000001
for x in range(1,1000001):
    fact[x] = md(fact[x-1] * x)
    invfact[x] = invMod(fact[x])

def comb(x,y):
    if(y < x): 
        return 0
    else:
        return md(fact[x] * invfact[y]) * invfact[x - y]

while True:
    try:
        n, a, b, d = str(input()).split()
        n = int(n)
        a = int(a)
        b = int(b)
        d = int(d)
        
        c1 = comb(n,a)
        c2 = comb(b,d)
        resp = md(c1* math.pow(c2, a, MOD))
        print(resp)
    except EOFError:
        pass
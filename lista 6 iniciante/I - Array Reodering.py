import math
casos = int(input())

for f in range(casos):
    ele = int(input())
    a = []
    par = []
    impar = []
    num = str(input()).split()
    for x in range(ele):
        if int(num[x]) % 2 == 0:
            par.append(int(num[x]))
        else:
            impar.append(int(num[x]))
    for x in range(len(par)):
        a.append(par[x])
    for x in range(len(impar)):
        a.append(impar[x])
    resp = 0
    for x in range(ele):
        for y in range(x + 1, ele):
            if (math.gcd(a[x],(2* a[y])) > 1):
                resp += 1
    print(resp)
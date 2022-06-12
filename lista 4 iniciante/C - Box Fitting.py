import bisect
c = int(input())
for x in range(c):
    n,w = str(input()).split()
    w = int(w)
    r = str(input()).split()
    lista = [None] * len(r)
    for i in range(len(r)):
        lista[i] = int(r[i])
    lista = sorted(lista)
    a = 1
    come = w
    while len(lista) != 0:
        z = (bisect.bisect_right(lista, come, hi=len(lista)))
        if(z < 1):
            come = w
            a+= 1
        else:
            z -= 1
            v = lista[z]
            come -= v
            lista.pop(z)
    print(a)
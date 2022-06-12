casos = int(input())

while casos > 0:
    casos -= 1
    n, k = str(input()).split()
    n = int(n)
    k = int(k)
    cont = 0
    b2 = n - 1
    b1 = n - 2
    rep = 1
    f = True
    while f:
        if k <= rep:
            b1 -= cont
            b2 -= (k - rep) + cont
            f = False
        else:
            rep +=  cont + 2
            cont += 1
    
    kString = ""
    for g in range(n):
        if g == b1 or g == b2:
            kString += "b"
        else:
            kString += "a"
    print(kString)
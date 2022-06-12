n = int(input())
for i in range(n):
    s = int(input())
    l = str(input()).split()
    mapa = [0] * (s+1)
    for a in range(s):
        l[a] = int(l[a])
        mapa[l[a]] = a
        if l[a] == s:
            x = a 
    saida = ""
    r = 0
    maxi = s
    while r < s:
        x = mapa[maxi]
        for j in range(x, s-r):
            saida += str(l[j]) + " "
            r += 1
        pm = mapa[maxi]
        while maxi >= 1 and pm <= mapa[maxi]:
            maxi -= 1
    print(saida)
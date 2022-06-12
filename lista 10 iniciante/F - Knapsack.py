casos = int(input())
for x in range(casos):
    n, w = list(map(int, input().split()))
    band = 0
    numeros = list(map(int, input().split()))
    q = 0
    s = 0
    dentro = []
    for d in range(n):
        if numeros[d] <= w:
            if(s + numeros[d] > w and numeros[d] * 2 < w):
                continue
            else:
                if (numeros[d] * 2 >= w):
                    q = d + 1
                    band = 1
                    break
                dentro.append(d + 1)
                s = s + numeros[d]
    
    if band == 0:
        if (len(dentro) != 0 and s*2 >= w and s <= w):
            print(len(dentro))
            saida = ""
            for y in dentro:
                saida += str(y) + " "
            print(saida)
        else:
            print("-1")
        continue
    else:
        print("1")
        print(q)
        continue
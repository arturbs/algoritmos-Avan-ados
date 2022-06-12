t = int(input())
for _ in range(t):
    a, k = list(map(int, input().split()))
    numeros = list(map(int, input().split()))
    inicio = 0
    fim = a - 1
    while k > 0 and inicio != fim:
        if numeros[inicio] == 0:
            inicio += 1
            continue
        else:
            numeros[inicio] -=1
            numeros[fim]+=1
            k-=1
    saida = ""
    for e in range(a):
        saida += str(numeros[e]) + " "
    print(saida)
casos = int(input())
for _ in range(casos):
    numeros = list(map(int, input().split()))
    a = numeros[0]
    b = numeros[1]
    n = numeros[2]

    atk = list(map(int, input().split()))
    vida = list(map(int, input().split()))
    combinacao = []
    for g in range(len(atk)):
        combina = [atk[g], vida[g]]
        combinacao.append(combina)
    combinacao.sort(key=lambda tup: tup[0])

    for r in range(n):
        if b <= 0 :
            break
        t1 = int(combinacao[r][1]/a)
        t2 = combinacao[r][1]%a
        t3 = int(b/combinacao[r][0])
        t4 = b%combinacao[r][0]
        if(t4 > 0):
            t3 += 1
        if(t2 > 0): 
            t1 += 1
        t1 = min(t1,t3)
        b -= t1*combinacao[r][0]
        combinacao[r][1] -= t1*a

    if(combinacao[n-1][1] > 0):
        print("NO")
    else:
        print("YES")
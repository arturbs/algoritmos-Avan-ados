N = 100005
w = [0 for _ in range(N)]
d = [0 for _ in range(N)]
casos = int(input())
for x in range(casos):
    
    n = int(input())
    trabalhos = list(map(int, input().split()))
    for i in range(1,n+1):
        w[i] = trabalhos[i-1]
        d[i] = 0
    for i in range(1,n):
        u,v = list(map(int, input().split()))
        d[u] += 1
        d[v] += 1

    resposta = 0
    
    v = []
    for i in range(1, n+1):
        resposta += w[i]
        for j in range(1, d[i]):
            v.append(w[i])
    v.sort(reverse=True)

    saida = ""
    saida += str(resposta) + " "
    for x in v:
        resposta += x
        saida += str(resposta) + " "
    print(saida)
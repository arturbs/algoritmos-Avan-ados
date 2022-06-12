#não passa nos testes

import heapq
q = []
tirar = []
soma = 0
band = True
numeros = list(map(int, input().split()))
n = numeros[0]
k = numeros[1]
precos = []
temprecos = list(map(int, input().split()))
for x in range(1,n+1):
    heapq.heappush(q, temprecos[x-1])
    soma += temprecos[x-1]
    if (x)%(k+1) == 0 :
        heapq.heappush(tirar, temprecos[x-1])
        soma -= temprecos[x-1]
        band = False
        
    if band:
        if len(tirar) > 0:
            menor = heapq.nsmallest(1, tirar)
            if menor[0] < temprecos[x-1]:
                soma += heapq.heappop(tirar)
                heapq.heappush(tirar, temprecos[x-1])
                soma -= temprecos[x-1]
    else:
        band = True
            
print(soma)
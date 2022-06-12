n, m = list(map(int, input().split())) 
atual = 1
resp = 0
destino = list(map(int, input().split())) 
memo = dict()

for x in range (m):
    if destino[x] >= atual:
        resp += destino[x] - atual
    else:
        resp += n - (atual - destino[x])
    atual = destino[x]
print(resp)
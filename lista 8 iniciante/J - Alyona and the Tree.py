from collections import deque
n = int(raw_input())
val = [0] + map(int,raw_input().split(" "))
maior = [0] * (n + 1)
g = [[] for _ in range(n + 1)]

for i in range(2, n+1):
    a,b = map(int,raw_input().split(" "))
    g[a].append((i,b))
    

resposta = 0
retira = [False] * (n+1)
pilha = deque([1])
while pilha:
    v = pilha.pop()
    if retira[v]:
        resposta += 1
    for u,d in g[v]:
        maior[u] = max(d, maior[v] + d)
        if maior[u] > val[u]:
            retira[u] = True
        else:
            retira[u] = retira[v]
        pilha.append(u)
print(resposta)
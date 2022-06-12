montes = int(input())
x = [None] * 101
y = [None] * 101
vertices = [None] * 101
resposta = -1

def dfs(a):
    vertices[a] = 1
    for i in range(1, montes + 1):
        if((x[i] == x[a] or y[i] == y[a]) and vertices[i] == None):
            dfs(i)
            
for p in range(1, montes + 1):
    posMonte = str(input()).split()
    x[p] = posMonte[0]
    y[p] = posMonte[1]
    
for o in range(1, montes + 1):
    if(vertices[o] == None):
        dfs(o)
        resposta += 1

print(resposta)
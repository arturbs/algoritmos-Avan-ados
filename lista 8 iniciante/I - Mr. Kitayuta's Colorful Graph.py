maxn = 105
n = 0
m = 0
q = 0
ff = [dict() for _ in range(maxn)]
resposta = [dict() for _ in range(maxn)]


def encontra( v, c):
    saida = 0
    if ff[v][c] == v:
        saida = v
    else:
        ff[v][c] = encontra(ff[v][c], c)
        saida = ff[v][c]
    return saida
    

def uniao( a, b, c):
    if c not in ff[a].keys():
        ff[a][c] = a
    if c not in ff[b].keys():
        ff[b][c] = b
    fa = encontra(a, c)
    fb = encontra(b, c)
    if fa != fb:
        ff[fa][c] = fb
        
def troca(x,y):
    y1 = x
    x1 = y
    y = y1
    x = x1
        

n, m = str(input()).split()
n = int(n)
m = int(m)
for k in range(m):
    a,b,c = str(input()).split()
    a = int(a)
    b = int(b)
    c = int(c)
    uniao(a, b, c)

    
q = int(input())
    
while (q) != 0:
    q -= 1
    x, y = str(input()).split()
    x = int(x)
    y = int(y)
    resp = 0
    if y in resposta[x].keys():
        print("{0:d}\n".format(resposta[x][y]), end = '')
        continue
    s1 = len(ff[x])
    s2 = len(ff[y])
    if s1 > s2:
        troca(x, y)
    for u in ff[x]:
        if u in ff[y].keys() and encontra(x, u) == encontra(y, u):
            resp += 1
    resposta[x][y] = resposta[y][x] = resp
    print("{0:d}\n".format(resp), end = '')
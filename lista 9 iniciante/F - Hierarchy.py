n = int(input()) 
funcionarios = str(input()).split()
m = int(input())

class node():
    def __init__(self):
        x = 0
        r = 0

N = 1005
infinito = 0x3f3f3f3f
posiFunc = [0 for _ in range(N)]
valorFunc = [0 for _ in range(N)]
vv = [list() for _ in range(N)]


def encontrar(x):
    r = x
    while posiFunc[r]!=r:
        r = posiFunc[r]
    i = x
    j = None
    while i!=r:
        j = posiFunc[i]
        posiFunc[i] = r
        i = j
    return r
 

for i in range(1,n+1):
    posiFunc[i] = i
    valorFunc[i] = int(funcionarios[i-1])

for i in range(m):
    contrato = node()
    aplicacao = str(input()).split()
    contrato.x = int(aplicacao[0])
    subalterno = int(aplicacao[1])
    contrato.r = int(aplicacao[2])
    if valorFunc[contrato.x] > valorFunc[subalterno]:
        vv[subalterno].append(contrato)
resposta = 0
for i in range(1,n+1):
    tem = infinito
    index = i
    for j in range(len(vv[i])):
        contrato = vv[i][j]
        if contrato.r<tem:
            tem = contrato.r
            index = contrato.x
    fx = encontrar(i)
    fy = encontrar(index)
    if fx!=fy:
        posiFunc[fx] = fy
        resposta+=tem
u = 2
while(u < n + 1):
    if encontrar(1)!=encontrar(u):
        break
    u += 1
if u > n:
    print(resposta)
else:
    print("-1")
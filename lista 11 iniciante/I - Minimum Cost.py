#errada, time limit exedido

def tamanhos(S, T, prim, seg):
    L = [[0 for i in range(seg + 1)]
            for i in range(prim + 1)]
             
    for i in range(prim + 1):
        for j in range(seg + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif S[i - 1] == T[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j],
                              L[i][j - 1])
    return L[prim][seg]
     

def menorCusto(S, T, custS, custT):
     
    prim = len(S)
    seg = len(T)
    tamanho = tamanhos(S, T, prim, seg)

    return (custS * (prim - tamanho) +
            custT * (seg - tamanho))
             

band = True
while(band):
    entrada1 = str(input())
    if entrada1 == '#':
        band = False
        break
    else:
        entrada2 = str(input())
        saida = menorCusto(entrada1, entrada2, 15, 30)
        print(saida)
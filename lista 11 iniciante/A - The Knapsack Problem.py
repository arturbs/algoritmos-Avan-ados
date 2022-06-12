def knapSack(maiorTamanhoPossivel, tamanhos, valores, n): 
    K = [[0 for x in range(maiorTamanhoPossivel + 1)] for x in range(n + 1)] 

    for i in range(n + 1): 
        for w in range(maiorTamanhoPossivel + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif tamanhos[i-1] <= w: 
                K[i][w] = max(valores[i-1] 
                          + K[i-1][w-tamanhos[i-1]],   
                              K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
   
    return K[n][maiorTamanhoPossivel] 
   
   
maiorTamanho, ni = list(map(int, input().split())) 
tamanhos = [0] * (ni + 1)
valores = [0] * (ni + 1)
for x in range (1, ni+1) :
    t,v = list(map(int, input().split())) 
    tamanhos[x] = t
    valores[x] = v

n = len(valores) 
print(knapSack(maiorTamanho, tamanhos, valores, n)) 
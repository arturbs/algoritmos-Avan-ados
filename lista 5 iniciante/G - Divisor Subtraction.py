#TIMELIMIT TESTE 5

import bisect
num = int(input())
cont = 0
def genPrimosSieve(numero):
    saida = ""
    primos = [True for i in range(numero+1)]
    p = 2
    while(numero >= p*p):
        if(primos[p] == True):
            for l in range(p*p,numero+1, p):
                primos[l] = False
        p+=1
    for p in range(2, numero+1):
        if primos[p]:
            saida += str(p) + " "
            
    saida = saida.split()   
    saida1 = [int(i) for i in saida]
    
    return saida1
    

if(num&1): 
    primos = genPrimosSieve(num+1)
    check = (bisect.bisect_right(primos, num ))
    num -= primos[check -1]
    cont +=1
         
cont += int(num/2)

print (cont)
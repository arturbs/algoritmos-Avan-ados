import bisect
n = int(input())
nums = str(input()).split()

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
            saida += str(p*p) + " "
    
    saida = saida.split()   
    saida1 = [int(i) for i in saida]
    
    return saida1

quadPrimos = genPrimosSieve(1000001)

for x in range(n):
    check = (bisect.bisect_right(quadPrimos, int(nums[x]) ))
    if (int(nums[x]) == quadPrimos[check - 1]):
        print("YES")
    else:
        print("NO")
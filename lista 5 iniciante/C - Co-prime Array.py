def mdcEuclidiano(x, y):
   while(y):
       x, y = y, x % y
   return x
   
def achaBigMC(x,y):
    t = True
    num = x+1
    while(t):
        if(mdcEuclidiano(x, num) == 1 and mdcEuclidiano(num, y) == 1):
            t = False
        else:
            num +=1
    return num

tam = int(input())
k = 0
arraySaida = ""
numeros = str(input()).split()
for x in range(tam-1):
    if(mdcEuclidiano(int(numeros[x]), int(numeros[x+1])) != 1):
        #novo = achaBigMC(int(numeros[x]), int(numeros[x+1]))
        novo = 1
        arraySaida += numeros[x] + " "
        arraySaida += str(novo) + " "
        k+=1
        
    else:
        arraySaida += str(numeros[x]) + " "
arraySaida += numeros[tam -1]     
print(k)
print(arraySaida)
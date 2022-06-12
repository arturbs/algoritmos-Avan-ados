#Não passou teste 6 errado

palavra = str(input())
separado = [char for char in palavra]

contA = 0
t = False
contEsp = 0
MOD = 1000000007

for x in range(len(separado)):
    if (separado[x] == "a"):
        contA += 1
        t = True
    if(separado[x] == "b" and t):
        contEsp += ((((2 ** (contA) ) - 1)%MOD)%MOD)
print(contEsp)




palavra = str(input())
separado = [char for char in palavra]
contB = 0
contEsp = 0
MOD = 1000000007

for x in range(len(separado) -1, -1, -1):
    if (separado[x] == "b"):
        contB = (contB + 1) % MOD
    else:
        contEsp = (contEsp + contB) % MOD
        contB = (contB * 2) 
print(contEsp)
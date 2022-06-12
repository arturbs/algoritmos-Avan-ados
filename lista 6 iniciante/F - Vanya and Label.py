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
        contB = (contB * 2) % MOD
print(contEsp)
#errado, time limit teste 5

m,n = str(input()).split()
m = int(m)
n = int(n)

a = str(input()).split()
b = str(input()).split()
somaA = 0
somaB = 0

for x in range(len(a)):
    somaA += int(a[x])
for x in range(len(b)):
    somaB += int(b[x])

if somaA > somaB:
    maior = somaA
    menor = somaB
else:
    maior = somaB
    menor = somaA
    
somaModA = somaA % n
somaModB = somaB % n
passos = 0
if maior - menor < m:
    for x in range(n + 2):  
        if somaModA == somaModB  and somaA + ((passos * m)%n) == somaB:
            print(passos)
            break
        else:
            somaModA = (somaModA + m) % n
            passos += 1
elif maior == somaB:
    for x in range(n + 2):  
        if somaModA == somaModB  and somaA + (passos * m) == somaB:
            print(passos)
            break
        else:
            somaModA = (somaModA + m) % n
            passos += 1
else:
    for x in range(n + 2):  
        if somaModA == somaModB  and somaB + (passos * m) == somaA:
            print(n - passos)
            break
        else:
            somaModA = (somaModA + m) % n
            passos += 1
n, m, k = str(input()).split()
n = int(n)
m = int(m)
k = int(k)

casas = str(input()).split()
c = [0] * (n+1)
saida = 0x3f3f3f3f

for x in range (1,len(casas)+1):
    c[x] = int(casas[x-1])

for x in range (m, n+1):
    if c[x]!=0:
        if c[x] <= k:
            saida = min(saida, (x-m)*10)
for x in range(m, 0, -1):
    if c[x]!=0:
        if c[x]<= k:
            saida = min(saida, (m-x)*10)
print(saida)
#uma forma melhor seria contar os numeros de sushis que estao em 
#grupos e fazer o maior das menores duplas de sushis, mas os testes
#passaram por tempo com while dentro de for
n = int(input())
s = str(input())
s = s.split(" ")
t = 0
rf = 0

for x in range(n):
    rt = 0
    f = 0
    while (f <= x and x + 1 + f < n):
        if s[x-f] != s[x + 1 + f] and s[x-f] == s[x] and s[x + 1 + f] == s[x + 1]:
            rt += 2
        else:
            break
        f += 1
        
    if (rf < rt):
        rf = rt
print(rf)
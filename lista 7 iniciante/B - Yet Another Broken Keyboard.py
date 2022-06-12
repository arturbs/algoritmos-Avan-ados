def somaPos(num):
    return (num * (num + 1))/2
n,k = str(input()).split()
n = int(n)
k = int(k)
ld = {}

pal = str(input())
s = [char for char in pal]

p = str(input()).split()
for z in range(len(p)):
    ld[p[z]] = 1

cont = 0
substrigs = 0
for x in range(len(s)):
    if s[x] in ld:
        cont += 1
    else:
        substrigs += somaPos(cont)
        cont = 0
substrigs += somaPos(cont)
cont = 0
print(int(substrigs))
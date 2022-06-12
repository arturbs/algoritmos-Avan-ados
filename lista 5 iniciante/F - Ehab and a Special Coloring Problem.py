n = int(input())
a = [None] * (n-1)
cont = 0
for h in range(n-1):
    if(a[h] == None):
        cont += 1
        for k in range(h, n-1, h + 2):
            a[k] = cont
            
saida = ""
for j in range( n - 1):
    saida += str(a[j]) + " "
print (saida)
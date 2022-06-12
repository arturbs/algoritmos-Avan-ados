#precisa de binary search

w,q = str(input()).split()
saida = ""
a = str(input()).split()
b = str(input()).split()
a1 = [int(i) for i in a]
a1 = sorted(a1)


for x in range(int(q)):
    c = 0
    for y in range(int(w)):
        if int(b[x]) < a1[y]:
            c = y 
            break
        if int(b[x]) >= a1[len(a1) - 1 - y]:
            c = len(a1) - y 
            break
        c += 1
    saida += str(c) + " "

print(saida[:len(saida) - 1])

# com binary search

import bisect
w,q = str(input()).split()
saida = ""
a = str(input()).split()
b = str(input()).split()
a1 = [int(i) for i in a]
a1 = sorted(a1)
c = ""

for x in range(int(q)):
    ru = int(b[x])
    c  += (str(bisect.bisect_right(a1, ru, hi=len(a1)) ) + " ")
    
print(c[:len(c) - 1])

n,m = str(input()).split()
a = ""
b = ""
for s in range(int(n)):
    a += str(input()) + " "
for t in range(int(m)):
    b += str(input()) + " "
    
a = a.split()
b = b.split()
iguais = 0

for i in range(int(n)):
    for o in range(int(m)):
        if a[i] == b[o]:
            iguais += 1

if iguais % 2 == 1:
    if (int(n) >= int(m)):
        print("YES")
    else:
        print("NO")
else:
    if int(m) >= int(n):
        print("NO")
    else:
        print("YES")
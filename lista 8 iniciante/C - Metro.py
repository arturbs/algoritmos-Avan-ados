n, s = str(input()).split()
s = int(s) - 1
n = int(n)
a = [None] * n
b = [None] * n

tempA = str(input()).split()
tempB = str(input()).split()

for x in range(n):
    a[x] = int(tempA[x])
    b[x] = int(tempB[x])

if (a[0] == 0):
    print("NO")

elif (a[s] == 1):
    print("YES")

elif (b[s] == 0):
    print("NO")
    
else:
    f = 0
    for h in range(n):
        if (a[h] == 1 and b[h] == 1):
            if h > s:
                f = 1
                break

    if f == 1:
        print("YES")
    else:
        print("NO")
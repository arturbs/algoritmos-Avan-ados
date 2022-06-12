n, t = str(input()).split()
t = int(t) - 1
n = int(n)
a = [None] * (n - 1)
atual = 0

tempA = str(input()).split()
for x in range(n-1):
    a[x] = int(tempA[x])
flag = True
while atual < t + 1:
    if atual == t:
        print("YES")
        flag = False
        break
    else:
        atual += int(a[atual])
if flag: 
    print("NO")
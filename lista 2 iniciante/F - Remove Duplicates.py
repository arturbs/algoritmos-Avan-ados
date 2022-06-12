n = int(input())
a = str(input()).split()
t = []
resposta = ""

for x in range(n-1, -1, -1):
    if a[x] in t:
        a.pop(x)
    else:
        t.append(a[x])
print(len(a))
for q in range(len(a)):
    resposta += a[q] + " "
print(resposta)
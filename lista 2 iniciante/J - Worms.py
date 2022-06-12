np = int(input())
p = str(input()).split()
j = int(input())
d = str(input()).split()

w = []
for u in range(np):
    w += [u+1] * int(p[u])

for i in range(j):
    print(w[int(d[i]) -1])
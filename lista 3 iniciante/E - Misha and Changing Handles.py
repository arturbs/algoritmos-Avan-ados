s = int(input())
c = []
for i in range(s):
    c.append(input())
dc = {}
cont = 0
for i in range(s-1, -1, -1):
    m = c[i].split()
    if m[1] in dc.keys():
        dc[m[0]] = dc.pop(m[1])
    else:
        dc[m[0]] = [m[1], cont]
        cont += 1 
r = [0] * len(dc)
for a in dc.keys():
    r[dc[a][1]] = a + " " + dc[a][0]
print(len(r))
for a in r:
    print(a)
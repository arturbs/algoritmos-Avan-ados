from sys import stdin,stdout
read,write = stdin.readline,stdout.write
p = [0] * 200000
size = [0]*200000

def init(m):
    for i in xrange(m):
        p[i] = i
        size[i] = 1
        
def find(a):
    if p[a] == a: return a
    p[a] = find(p[a])
    return p[a]
def uniao(a,b):
    a,b = find(a), find(b)
    if a != b:
        if size[a] < size[b]: a,b = b,a
        p[b] = a
    size[a] += size[b]
    
m,n = map(int, read().split())

while (m!=0):
    init(m)
    edges = []
    somaMST = 0
    somaTotal = 0
    for i in xrange(n):
        u,v,w = raw_input().split()
        u = int(u)
        v = int(v)
        w = int(w)
        edges.append((w,v,u))
    edges.sort()
    for w, u, v in edges:
        u,v = find(u), find(v)
        somaTotal += w
        if u != v:
            somaMST += w
            uniao(u,v)
    print(somaTotal - somaMST)
    m,n = map(int, read().split())
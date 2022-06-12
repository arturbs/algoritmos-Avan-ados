import sys
sys.setrecursionlimit(10**5)
from collections import deque

n, m = str(input()).split()
n = int(n)
m = int(m)

cor = [0 for _ in range(n)]
grid = [None for _ in range(n)]
g = [list() for _ in range(n)]

for u in range(n):
    grid[u] = [None for _ in range(m)]
    g[u] = [list() for _ in range(m)]
    cor[u] = [0 for _ in range(m)]
    ent = str(input())
    entrada = [char for char in ent]
    for q in range(len(entrada)):
        grid[u][q] = entrada[q]
    
for i in range(n):
    for j in range(m):
        if i and grid[i][j] == grid[i-1][j]:
            g[i][j].append((i-1,j))
        if j and grid[i][j] == grid[i][j-1]:
            g[i][j].append((i,j-1))
        if i < n-1 and grid[i][j] == grid[i+1][j]:
            g[i][j].append((i+1,j))
        if j < m-1 and grid[i][j] == grid[i][j+1]:
            g[i][j].append((i,j+1))

def ciclo(i,j,pre):
    cor[i][j] = 1
    for v in g[i][j]:
        if v == pre: 
            continue
        if cor[v[0]][v[1]] == 0:
            ciclo(v[0], v[1], (i,j))
        if cor[v[0]][v[1]] in [1,3]:
            cor[i][j] = 3
    if cor[i][j] == 1:
        cor[i][j] = 2
        
cic = "No"
for i in range(n):
    for j in range(m):
        if cor[i][j] == 0:
            ciclo(i,j,(-1,-1))
            if cor[i][j] == 3:
                cic = "Yes"
print(cic)
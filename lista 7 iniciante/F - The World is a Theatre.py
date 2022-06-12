#errado, wrong answer on test 5

n,m,t = str(input()).split()
n = int(n)
m = int(m)
t = int(t)

def variacoes(n,m):
    va = 1
    for x in range(m):
        va *= (n-x)/(x+1)
    return va
    
equipes = 0
for r in range(4, t):
    equipes += variacoes(n,r) * variacoes(m, t - r)
print(int(equipes))
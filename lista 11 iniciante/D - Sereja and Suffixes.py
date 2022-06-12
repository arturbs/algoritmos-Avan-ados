#errado, runtime error test 1

n, m = list(map(int, input().split()))
maxim = 10005
temp1 = [False]  *  maxim
temp2 = [0] * maxim

elementos = list(map(int, input().split()))

for x in range(n,0,-1):
    if(temp1[elementos[x-1]] == False):
        temp2[x-1] += 1
    temp1[elementos[x-1]] = True

for y in range(n,0,-1):
    temp2[y-1] += temp2[y]
    
for u in range(m):
    t = int(input())
    print(temp2[t-1])
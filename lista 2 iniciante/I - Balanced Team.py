m = int(input())
team = str(input()).split()

teamOrder = [int(i) for i in team]
teamOrder.sort()
    
bigTeam = 0
k = 0
for x in range(m):
    while k < m and teamOrder[k] - teamOrder[x] <= 5:
        k += 1
    if bigTeam < k-x:
        bigTeam = k-x

print(bigTeam)
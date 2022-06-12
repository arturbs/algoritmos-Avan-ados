n, k = str(input()).split()
n = int(n)
k = int(k)

robots = str(input()).split()

count = 1
while True:
    if k-count <= 0:
        print(robots[k-1])
        break
    k -= count
    count+=1
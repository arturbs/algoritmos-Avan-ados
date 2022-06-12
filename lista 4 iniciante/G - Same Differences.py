cases = int(input())

for x in range(cases):
    size = int(input())
    num = str(input()).split()
    n = {}
    for v in range(len(num)):
        if (int(num[v]) - v not in n):
            n[int(num[v]) - v] = 1
        else:
            n[int(num[v]) - v] += 1
    con = 0
    
    for key in n:
        while n[key] > 1:
            con += n[key] - 1
            n[key] -= 1
    
    print(con)
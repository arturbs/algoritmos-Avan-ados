n = int(input())
t1 = 0
for i in range(3):
    s = str(input()).split()
    t = 0
    for a in s:
        t += int(a)
    if i!=0:
        print(t1 - t)
    t1 = t
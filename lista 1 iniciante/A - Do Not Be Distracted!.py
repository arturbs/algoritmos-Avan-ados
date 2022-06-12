repeat = int(input())
for x in range(repeat):
    t = int(input())
    w = str(input())
    m = []
    c = True
    for y in range(t):
        if w[y]  in m:
            if w[y] != w[y-1]:
                c = False
                break
        else:
            m.append(w[y])
    if(c):
        print("YES")
    else:
        print("NO")
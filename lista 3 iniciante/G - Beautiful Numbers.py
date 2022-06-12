n = int(input())

for i in range(n):
    s = int(input())
    l = str(input()).split()

    m = [None] * (s+1)
    for a in range(s):
        l[a] = int(l[a])
        m[l[a]] = a
        if l[a] == 1:
            x = a
            y = a

    r = ["0"] * (s+1)

    r[1] = "1"
    for b in range(2, s+1):
        x = min(m[b], x)
        y = max(m[b], y)

        if y - x +1 <= b:
            r[b] = "1"
    rstr = ""
    for j in range(1, s+1):
        rstr += r[j]

    print(rstr)
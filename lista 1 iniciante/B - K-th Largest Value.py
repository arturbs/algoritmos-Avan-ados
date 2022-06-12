n, q = str(input()).split()
n = int(n)
q = int(q)

s = str(input())
s = s.split(" ")


for x in range(q):
    t, w = str(input()).split()
    t = int(t)
    w = int(w)
    if t == 1:
        s[w - 1] = 1 - int(s[w -1])
    else:
        count = 0
        for y in range(q):
            if int(s[y]) == 1:
                count += 1
        if count >= w:
            print("1")
        else:
            print("0")
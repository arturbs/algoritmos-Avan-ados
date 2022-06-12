n, m = str(input()).split()

c = int(n) * int(n)
l = [0] * int(n)
col = [0] * int(n)
r = ""
p = 0
nl = 0
ncol = 0

conhe = 0
for i in range(int(m)):
    x, y = str(input()).split()
    x = int(x)-1
    y = int(y)-1

    if  col[x] == 0:
        col[x] = 1
        ncol += 1
        conhe += nl
        p += int(n)

    if l[y] == 0:
        l[y] = 1
        nl += 1
        conhe += ncol
        p += int(n)

    r += str(c - p + conhe) + " "
print(r)
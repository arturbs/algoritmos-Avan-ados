s = int(input())
h = str(input())
q = [0,0,0,0,0,0,0,0,0,0]
l = 0
r = 9

for i in h:
    if i == "R":
        q[r] = 1
        while q[r] != 0:
            if r == 0:
                l = 9
                break
            r -= 1
    elif i == "L":
        q[l] = 1
        while q[l] != 0:
            if l == 9:
                r = 0
                break
            l += 1
    else:
        num = int(i)
        q[num] = 0
        if l > num:
            l = num
        if r < num:
            r = num

saida = ""
for i in q:
    saida += str(i)
print(saida)
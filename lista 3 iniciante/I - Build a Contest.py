n,m = str(input()).split()
d = {}
q = str(input()).split()

s = ""

for x in range(int(m)):
    a = int(q[x]) 
    if a not in d:
        d[a] = 1
    else:
        d[a] += 1
    yu = len(d)
    if(len(d) == int(n)):
        for l in range (int(n)):
            d[l + 1] -= 1
            if d[l + 1] == 0:
                d.pop(l+1)
        s += "1"
    else :
        s += "0"
        
print(s)
n, k = str(input()).split()
pstr = str(input()).split()
p = ""

for i in range(int(n)):
    p += (str(pstr[i])) + " "
    
p = p.split()

vs = 0
a = int(p[0])
for i in range(1,int(n)):
    if int(p[i]) > a:
        vs = 1
        a = int(p[i])
    else:
        vs += 1
    if vs == int(k):
        break

print(a)
z = int(input())
p = str(input()).split()
v = int(input())

p1 = [int(i) for i in p]
p1 = sorted(p1)

sp = [0]
sp.append(int(p[0]))
sp1 = [0]
sp1.append(int(p1[0]))

for u in range(1,len(p)):
    sp.append( int(p[u]) + sp[u])
    
for o in range(1,len(p1)):
    sp1.append(int(p1[o] + sp1[o]))
for x in range(v):
    q = str(input()).split()
    q1 = int(q[0])
    q2 = int(q[1]) 
    q3 = int(q[2])

    if q[0] == "1":
        print (sp[q3 ] - sp[q2 - 1])
    else:
        print (sp1[q3 ] - sp1[q2 -1])
import math

a = str(input()).split()
b = str(input()).split()
c = str(input()).split()
ax = int(a[0])
ay = int(a[1])
bx = int(b[0])
by = int(b[1])
cx = int(c[0])
cy = int(c[1])
caminho = (ax - bx) * (cy - by) - (ay - by) * (cx - bx)

if caminho > 0:
    print("RIGHT")
elif caminho < 0:
    print("LEFT")
else:
    print("TOWARDS")
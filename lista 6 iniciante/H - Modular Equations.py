MOD = 1000000007
a, b = str(input()).split()
a = int(a)
b = int(b)
cont = 0

if (a == b):
    print("infinity")
elif(a<b):
    print(cont)
else:
    a -= b
    c = 1
    while c*c <= a:
        if a%c == 0:
            if c > b:
                cont += 1
            if a/c > b and c*c != a:
                cont += 1
        c += 1
    print(cont)
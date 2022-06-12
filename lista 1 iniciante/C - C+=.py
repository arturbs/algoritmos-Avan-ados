repeat = int(input())
x = repeat

for t in range(repeat):
    operations = 0
    e = str(input())
    e = e.split(" ")
    a = int(e[0])
    b = int(e[1])
    n = int(e[2])
    while (a <= n and b <= n):
    
        if a >= b:
            b = b + a
            operations = operations + 1
        else:
            a = a + b
            operations = operations + 1
    print (operations)
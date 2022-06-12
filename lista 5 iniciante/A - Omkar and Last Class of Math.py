import math 
casos = int(input())

for p in range(casos):
    saida =""
    n = int(input())
    t = 0
    supo = math.sqrt(n + 0.1)
    for f in range(2, int(supo) + 1):
        if (n%f == 0):
            t = 1
            t1 = f
            if (n/f > t) :
                t = n/f
                saida += str(int(t)) + " " + str(int(n-t))
                print(saida)
                break
    if (t == 0):
        saida += "1 " + str(int(n-1))
        print(saida)
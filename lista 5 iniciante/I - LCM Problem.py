casos = int(input())

for x in range(casos):
    numeros = str(input()).split()
    l = int(numeros[0])
    r = int(numeros[1])
    if(l * 2 > r):
        print("-1 -1")
    else:
        print(str(l) + " " + str(l * 2))
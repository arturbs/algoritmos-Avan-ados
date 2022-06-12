cases = int(input())

for c in range(cases):
    n, m = str(input()).split()
    pre = str(input()).split()
    des = str(input()).split()
    javaMapa = {}
    cont = 1
    for f in range (len(pre)):
        javaMapa[pre[f]] = cont
        cont += 1
    temp = 0
    maior = 0
    retirados = 0
    
    for x in range (int(m)):
        if javaMapa[des[x]] < maior:
            temp += 1
            retirados += 1
        else:
            temp += ((javaMapa[des[x]] - 1 - retirados) * 2) + 1
            retirados += 1
        if javaMapa[des[x]] > maior:
            maior = javaMapa[des[x]]
    print(temp)
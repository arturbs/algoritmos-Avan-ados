#não passou por tempo

h = True
while h:
    pilha = list()
    maior = 0
    h = str(input()).split()
    if h[0] == "0":
        break
    h = h[1:len(h)]
    
    x = 0
    while x < len(h):
        if (not pilha) or (int(h[pilha[-1]]) <= int(h[x])):
            pilha.append(x)
            x += 1
        else:
            topo = pilha.pop()
            area = (int(h[topo]) * ((x- int(pilha[-1]) -1) if pilha else x))
            if maior < int(area):
                maior = int(area)
    while pilha:
        topo = pilha.pop()
        area = (int(h[topo]) * ((x- int(pilha[-1]) -1) if pilha else x))
        if maior < int(area):
            maior = int(area)
    print(maior)
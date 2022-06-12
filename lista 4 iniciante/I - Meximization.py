cases = int(input())
for l in range(cases):
    size = int(input())
    ordem = str(input()).split()
    s = [int(i) for i in ordem]
    s = sorted(s)
    saida = [None] * len(s)
    saida[0] = s[0]
    x = 1
    contador = 0
    while x < len(s):
        if s[x] == s[x-1]:
            saida[len(s) - 1 - contador] = s[x]
            contador +=1 
            x += 1
            
        
        else:
            saida[x-contador] = s[x]
            x +=1
            
    saida1 = ""
    for o in saida:
        saida1 += str(o) + " "
    print(saida1)
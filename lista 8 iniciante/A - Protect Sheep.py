r, c = str(input()).split()
r = int(r)
c = int(c)
flag = True
pasto = [None] * r
for j in range(r):
    pasto[j] = [None] * c
    entr = str(input())
    entrada = [char for char in entr]
    for g in range(len(entrada)):
        pasto[j][g] = entrada[g]
for k in range(len(pasto)):
    for l in range(len(pasto[k])):
        if pasto[k][l] == "S":
            if (k + 1 < r):
                if(pasto[k+1][l] == "W"):
                    flag = False
                elif(pasto[k+1][l] == "."):
                    pasto[k+1][l] = "D"
            if (k-1 > -1):
                if(pasto[k-1][l] == "W"):
                    flag = False
                elif(pasto[k-1][l] == "."):
                    pasto[k-1][l] = "D"
            if(l-1 > -1):
                if(pasto[k][l-1] == "W"):
                    flag = False
                elif(pasto[k][l-1] == "."):
                    pasto[k][l-1] = "D"
            if(l+1 < c):
                if(pasto[k][l+1] == "W"):
                    flag = False
                elif(pasto[k][l+1] == "."):
                    pasto[k][l+1] = "D"
                
                
if flag:
    print("Yes")
    for u in range(len(pasto)):
        saida = ""
        for w in range(len(pasto[u])):
            saida += pasto[u][w]
        print(saida)
    
else:
    print("No")
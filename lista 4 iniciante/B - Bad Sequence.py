n = int(input())
c = str(input())
saida = "Yes"

if n % 2 == 1:
    saida = "No"
else:
    cont = 0
    for i in c:
        if i == "(":
            cont += 1
        else:
            cont -= 1
        if cont < -1:
            saida = "No"
            break

    if cont > 1:
        saida = "No" 
print(saida)
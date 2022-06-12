nc = int(input())
eixox = str(input()).split()

for x in range(nc):
    menor = 0
    maior = 0
    if(x==0):
        menor = - (int(eixox[x]) - int(eixox[x+1]))
        maior = - (int(eixox[x]) - int(eixox[nc-1]))
    if (x==nc-1):
        menor = - (int(eixox[x-1]) - int(eixox[x]))
        maior = - (int(eixox[0]) - int(eixox[x]))
    if (menor == 0):
        if(-(int(eixox[x-1]) - int(eixox[x])) < -(int(eixox[x]) - int(eixox[x+1]))):
            menor = -(int(eixox[x-1]) - int(eixox[x]))
        else:
            menor = -(int(eixox[x]) - int(eixox[x+1]))
    if(maior ==0):
        if(-(int(eixox[0]) - int(eixox[x])) > -(int(eixox[x]) - int(eixox[nc-1]))):
            maior = -(int(eixox[0]) - int(eixox[x]))
        else:
            maior = -(int(eixox[x]) - int(eixox[nc-1]))
                

    print(str(menor) + " " + str(maior)) 
empregados = int(input())
relacao = {}

for x in range(empregados):
    relacao[x+1] = int(input())

niveis = {}

for x in range(empregados):
    cont = -1
    funcionario = x+1
    chefe = 0
    while chefe != -1:
        chefe = relacao[funcionario]
        funcionario = relacao[funcionario]
        cont += 1
          
    if cont in niveis:
        niveis[cont] += 1
    else:
        niveis[cont] = 1

print(len(niveis))
tamanhoDaPilha = int(input())

pilhaDeLivros = str(input())
mochila = str(input())
pilhaDeLivros = pilhaDeLivros.split(" ")
mochila = mochila.split(" ")

movimentos = ""
ordemMochila = [None] * tamanhoDaPilha
for i in range(tamanhoDaPilha):
    ordemMochila[int(pilhaDeLivros[i])-1] = i + 1

y = 0
for l in mochila:
    x = int(l) - 1
    if ordemMochila[x] < y:
        movimentos += ("0 ")
    else:
        movimentos += str(ordemMochila[x]-y) + " "
        s = ordemMochila[x]

print(movimentos)
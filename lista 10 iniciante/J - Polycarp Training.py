concursos = int(input())
questoes = list(map(int, input().split()))
analise = {}
for x in range(len(questoes)):
    if questoes[x] not in analise:
        analise[questoes[x]] = 1
    else:
        analise[questoes[x]] += 1

lista = []
for k, v in analise.items():
    lista.append((k,int(v)))

lista = sorted(lista, key=lambda tup: tup[0])
band = True
suporte = 0
questoesDesejadas = 1
resposta = 0
while band:
    if suporte > len(lista) - 1:
        break
    if lista[suporte][0] >= questoesDesejadas and lista[suporte][1] > 0:
        lista[suporte] =  (lista[suporte][0],lista[suporte][1]-1)
        resposta += 1
        questoesDesejadas += 1
    else:
        suporte += 1
    

print(resposta)
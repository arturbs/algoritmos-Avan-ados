num = int(input())
nomes = []
dic = {}

for x in range(num):
    nome = str(input())
    nomes.append(nome)
    
for y in range(len(nomes)- 1, -1,-1):
    if ((nomes[y] not in dic)) :
        print(nomes[y])
    dic[nomes[y]] = 1
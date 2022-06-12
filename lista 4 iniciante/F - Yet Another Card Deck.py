# não passou por tempo teste 7
n, q = str(input()).split()
cores = str(input()).split()
desejo = str(input()).split()
pilhaDeCores = []
for f in range (len(cores) -1 , -1, - 1):
    pilhaDeCores.append(cores[f])
respo = ""

for d in range (int(q)):
    for x in range(len(pilhaDeCores) -1 , -1, - 1):
        if pilhaDeCores[x] == desejo[d]:
            temp = pilhaDeCores.pop(x)
            pilhaDeCores.append(temp)
            respo += str(len(pilhaDeCores) - x) + " "
            break
print(respo)

# não passou por tempo teste 4

n, q = str(input()).split()
cores = str(input()).split()
desejo = str(input()).split()
pilhaDeCores = {}
for f in range (len(cores)):
    if cores[f] not in pilhaDeCores:
        pilhaDeCores[cores[f]] = f + 1
respo = ""
maior = 0
topo = cores[0]

for d in range (int(q)):
    posicao = pilhaDeCores[desejo[d]]
    respo += str(posicao) + " "
    for key, value in pilhaDeCores.items():
        if value < posicao:
            pilhaDeCores[key] = value + 1
    pilhaDeCores[desejo[d]] = 1
print(respo)

# não passou no teste 4

n, q = str(input()).split()
cores = str(input()).split()
desejo = str(input()).split()
pilhaDeCores = []
for f in range (len(cores) -1 , -1, - 1):
    pilhaDeCores.append(cores[f])
respo = ""

d = 0
while d < int(q):
    for x in range(len(pilhaDeCores) -1 , -1, - 1):
        if pilhaDeCores[x] == desejo[d]:
            temp = pilhaDeCores.pop(x)
            pilhaDeCores.append(temp)
            respo += str(len(pilhaDeCores) - x) + " "
            
            if d+1 < len(desejo):
                u = True
                o = 0
                while u and d < len(desejo) - 2:
                    if (desejo[d] == desejo[d+1]):
                        respo += "1 "
                        d +=1
                    else:
                        u = False
            d +=1
            break
            
print(respo)

# não passou no teste 7
n, q = str(input()).split()
cores = str(input()).split()
desejo = str(input()).split()
pilhaDeCores = []
for f in range (len(cores) -1 , -1, - 1):
    pilhaDeCores.append(cores[f])
respo = ""

for d in range (int(q)):
    for x in range(len(pilhaDeCores) -1 , -1, - 1):
        if pilhaDeCores[x] == desejo[d]:
            if x == len(pilhaDeCores) - 1:
                respo +=  "1 "
                break
            else:
                temp = pilhaDeCores.pop(x)
                pilhaDeCores.append(temp)
                respo += str(len(pilhaDeCores) - x) + " "
                break 
            
print(respo)


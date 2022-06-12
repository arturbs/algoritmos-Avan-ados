z = int(input())

for x in range(z):
    a = str(input())
    a += "0"
    a = [char for char in a]
    cont = 0
    sizes = []
    for b in range(len(a)):
        if int(a[b]) == 1:
            cont += 1
        else:
            sizes.append(cont)
            cont = 0
           
    sizes.sort(reverse=True)
    soma = 0
    for l in range(0,len(sizes), +2):
        soma += int(sizes[l])
    print (soma)
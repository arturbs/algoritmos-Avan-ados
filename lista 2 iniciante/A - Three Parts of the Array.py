n = int(input())
lista = str(input()).split()

i = 0
j = n - 1
sum1 = int(lista[i])
sum3 = int(lista[j])
maximo = 0
while i < j:
    if sum1 < sum3:
        i += 1
        sum1 += int(lista[i])
    elif sum1 > sum3:
        j -= 1
        sum3 += int(lista[j])
    else:
        maximo = sum1
        i += 1
        sum1 += int(lista[i])

print(maximo)
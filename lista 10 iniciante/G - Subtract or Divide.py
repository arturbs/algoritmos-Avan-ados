def decide(numero):
    if numero == 1:
        return 0
    elif numero == 2:
        return 1
    elif numero == 3:
        return 2
    elif numero&1:
        return 3
    else:
        return 2

casos = int(input())

for q in range(casos):
    numero = int(input())
    print(decide(numero))
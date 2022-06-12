def crescente(lista):
    bandeira = True
    for x in range(len(lista)-1):
        if lista[x] < lista[x+1]:
            continue
        else:
            bandeira = False
            break
    return bandeira
    
def tentaCrescente(lista):
    for x in range(len(lista)-1):
        passa = lista[x] - x
        if passa < 0:
            return False
        lista[x] = x
        lista[x+1] += passa
    
    return crescente(lista)

casos = int(input())

for x in range(casos):
    qtpilhas = int(input())
    pilhas = list(map(int, input().split()))
    if crescente(pilhas):
        print("YES")
    else:
        if tentaCrescente(pilhas):
            print("YES")
        else:
            print("NO")
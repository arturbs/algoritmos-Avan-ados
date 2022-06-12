#não passou por tempo

cases = int(input())

def retira(e, s):
    
    x = 0
    while x < len(e) - 1:
        if e[x+1] == "B":
            e.pop(x)
            e.pop(x)
            b = True
            while b:
                if (len(e) > 1 and x < len(e)):
                    if ( (e[x] != "B") or x < 1):
                        b = False
                    else:
                        e.pop(x-1)
                        e.pop(x-1)
                        x -= 1 
                else:
                    b = False
        else:
            x += 1
    print(len(e))
        
for x in range(cases):
    ent = str(input())
    e = [char for char in ent]
    s = False
    retira(e, s)

#outra abordagem

cases = int(input())

for x in range(cases):
    contador = 0
    ent = str(input())
    e = [char for char in ent]
    
    for y in range(len(e)):
        if e[y] == "A" or contador == 0:
            contador +=1
        else:
            contador -= 1
    print(contador)
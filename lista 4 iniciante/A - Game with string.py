ent = str(input())
e = [char for char in ent]
s = False
def retira(e, s):
    
    x = 0
    while x < len(e) - 1:
        if e[x] == e[x+1]:
            e.pop(x)
            e.pop(x)
            s = not s
            b = True
            while b:
                if (len(e) > 1 and x < len(e)):
                    if (e[x - 1] != e[x] or x < 1):
                        b = False
                    else:
                        e.pop(x-1)
                        e.pop(x-1)
                        x -= 1
                        s = not s  
                else:
                    b = False
        else:
            x += 1
    if s:
        print("Yes")
    else:
        print("No") 

retira(e, s)
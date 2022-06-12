t = int(input())

for x in range(t):
    s1 = str(input())
    s2 = str(input())
    tamanho = len(s1)
    s1 = list(s1)
    s1.sort()
    f = False;
    
    
    for y in range(len(s2) - len(s1) + 1):
        if s2[y] in s1:
            test = list(s2[y:y+len(s1)])
            test.sort()
            if test == s1:
                f = True
                break
      
    if not f :
        print("NO")
    else:
        print("YES")
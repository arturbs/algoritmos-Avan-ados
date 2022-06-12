x = int(input())
f = True

for a in range(1, x +1):
    if f:
        for b in range(1, x+1):
            if (a % b == 0) and (a*b > x) and  (a/b < x):
                print(str(a) + " " + str(b))
                f = False
                break
                        
    else:
        break
    
if f :
    print("-1")
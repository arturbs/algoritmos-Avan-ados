import math 
def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)  
num = int(input())
div = int(math.sqrt(num))
s = 0
if (num == 1 or num == 0):
    s= 1
    print(s)
else:
    for g in range(1, div + 1):
        if(num%g == 0):
            s += 2
    if(div * div == num):
        s -= 1
    print(s)
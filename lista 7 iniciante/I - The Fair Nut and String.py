MOD = 1000000007

def M(x): 
    return ((x%MOD) + MOD) % MOD
    
string = str(input())

s = [char for char in string]
res = 1
cont = 1
for x in s:
    if x == "a":
        cont +=1
    elif x == "b":
        res = M(res*cont)
        cont = 1
res = M(res*cont)

print(M(res - 1))
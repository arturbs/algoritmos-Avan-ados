n, m = str(input()).split()
n = int(n)
m =int(m)
resposta = 0

while n < m:
    if (int(m)&1) :
        m += 1
    else:
        m /= 2
    resposta +=1
resposta += n-m 
    
print(int(resposta))
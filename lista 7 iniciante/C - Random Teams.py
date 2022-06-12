#errada, wrong answer test 11

n,m = str(input()).split()
n = int(n)
m = int(m)

def somaPares(final):
    return (final * (final - 1))/2
    
menorT = int(n/m) 
qtdT = n % m
mini = qtdT * somaPares(menorT + 1) + ((m - qtdT) * somaPares(menorT))

maiorT = n - (m-1)
maxi = somaPares(maiorT)

print(str(int(mini)) + " " + str(int(maxi)))
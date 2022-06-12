import math
casos = int(input())

for x in range(casos):
    k = int(input())
    lagua = 100 - k
    lmagica = k
    relacao = math.gcd(lmagica,lagua)
    lagua /= relacao
    lmagica /= relacao
    passos = int(lagua + lmagica)
    print(passos)
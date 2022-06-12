w = str(input())
w = list(w)
v = 0
vogal = "aeiou"
impar = "13579"

for x in range(len(w)):
    if w[x] in vogal or w[x] in impar:
        v += 1
print(v)
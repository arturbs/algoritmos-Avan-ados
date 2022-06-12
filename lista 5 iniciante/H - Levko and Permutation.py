num = str(input()).split()
f = True

if (num[0] == num[1] or int(num[1]) > int(num[0])):
   f = False

a = int(num[0])
b = int(num[1])
saida = str(a - b) + " "
for x in range(a - b - 1):
    saida += str(x+1) + " "
for y in range(a-b + 1, a + 1):
    saida += str(y) + " "

if (f):
    print(saida)
else:
    print("-1")
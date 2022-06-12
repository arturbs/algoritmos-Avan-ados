r = int(input())
saida = ""
if (r&1 and r> 3):
    x = str(1) + " "
    y = str(int((r-3)/2))
    saida += x + y
else:
    saida += "NO"
print(saida)
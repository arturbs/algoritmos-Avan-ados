#errada, wrond answer test 8

caminhos = int(input())
s = 1
for x in range(5):
    s = s*(caminhos - x)
s /= 120
saida = int(s*s*120)
print(saida)
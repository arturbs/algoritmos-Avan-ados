import string
qtAlunos = int(input())
turma1 = dict.fromkeys(string.ascii_lowercase, 0)
turma2 = dict.fromkeys(string.ascii_lowercase, 0)
alfabeto = string.ascii_lowercase
for x in range(qtAlunos):
    aluno = str(input())
    a = [char for char in aluno]
    if turma1[a[0]] == turma2[a[0]]:
        turma1[a[0]] += 1
    else:
        turma2[a[0]] += 1

possi = 0
for y in range(len(turma1)):
    if turma1[alfabeto[y]] > 1:
        possi += (turma1[alfabeto[y]] * (turma1[alfabeto[y]] - 1 ))/2
    if turma2[alfabeto[y]] > 1:
        possi += (turma2[alfabeto[y]] * (turma2[alfabeto[y]] - 1 ))/2
print(int(possi))
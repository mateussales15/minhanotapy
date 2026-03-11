import random;
alunos = input("Alunos: ").split()
quantTrimestre = int(input("Quantidade de Trimestres: "))

for aluno in alunos:
    notasTrimestre = 0
    for i in range(1, 4):
        valor = random.randint(1, 100)
        print(aluno + str(i) + " | " + str(valor))
        notasTrimestre += valor
    if notasTrimestre / quantTrimestre >= 60:
        print("Passou ✅")
    else:
        print("Não passou ❌")
        print("Faltou: " + str(60 - notasTrimestre / quantTrimestre))
import random

a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))

print('Qual sera a ordem de apresentacao dos trabalhos?')

alunos = [a1, a2, a3, a4]

random.shuffle(alunos)

print(f'A ordem de apresentacao dos trabalhos sera {alunos}')
from random import randint

machine_num = randint(0, 5)
user_num = int(input('Eu pensei em um numero entre 0 e 5, consegue adivinhar qual eh? '))

if user_num == machine_num :
    print('PARABENS, VOCE ACERTOU!!!')
else :
    print('Que pena... voce errou')

print(f'O numero selecionado era: {machine_num}')
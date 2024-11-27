from time import sleep
from secrets import choice

jokenpo = ['pedra', 'papel', 'tesoura']

# JOKENPO
bot_choice = (choice(jokenpo))

print('Vamos jogar JOKENPO? Digite o numero correspondente:')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')
user_choice = int(input())

print('Pronto?')
sleep(1)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
sleep(1)

print(f'{bot_choice.upper()}!!!')
sleep(0.6)
if user_choice == 1 and bot_choice == 'tesoura':
    print(f'Voce ganhou! Eu escolhi {bot_choice}')
elif user_choice == 1 and bot_choice == 'papel':
    print(f'Voce perdeu! Eu escolhi {bot_choice}')
elif user_choice == 1 and bot_choice == 'pedra':
    print(f'Empatamos! Eu escolhi {bot_choice}')
elif user_choice == 2 and bot_choice == 'pedra':
    print(f'Voce ganhou! Eu escolhi {bot_choice}')
elif user_choice == 2 and bot_choice == 'tesoura':
    print(f'Voce perdeu! Eu escolhi {bot_choice}')
elif user_choice == 2 and bot_choice == 'papel':
    print(f'Empatamos! Eu escolhi {bot_choice}')
elif user_choice == 3 and bot_choice == 'papel':
    print(f'Voce ganhou! Eu escolhi {bot_choice}')
elif user_choice == 3 and bot_choice == 'pedra':
    print(f'Voce perdeu! Eu escolhi {bot_choice}')
elif user_choice == 3 and bot_choice == 'tesoura':
    print(f'Empatamos! Eu escolhi {bot_choice}')

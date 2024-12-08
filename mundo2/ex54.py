from datetime import datetime

actual_year = datetime.now().year

maior = 0
menor = 0

for x in range(1,8):
    idade = (actual_year - int(input(f'Em que ano a {x} pessoa nasceu = ')))
    if idade >= 18:
        maior += 1
    elif idade < 18:
        menor += 1

print(f'{maior} pessoas sao maiores de idade, enquanto {menor} pessoas sao menores de idade')
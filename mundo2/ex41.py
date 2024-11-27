from datetime import date

idade = date.today().year - int(input('Digite o ano em que nasceu: '))


print(f'{idade} anos')

if idade <= 9:
    print(f'MIRIM')
elif idade >= 10 and idade <= 14:
    print(f'INFANTIL')
elif idade >= 15 and idade <= 19:
    print(f'JUNIOR')
elif idade > 19 and idade <= 20:
    print(f'SENIOR')
else:
    print(f'MASTER')
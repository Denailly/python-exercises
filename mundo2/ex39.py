import datetime

idade = datetime.date.today().year - int(input('Digite o ano em que nasceu: '))

if idade < 18:
    print(f'Voce tem {idade} anos, ainda faltam {18 - idade}anos para voce precisar se alistar')
elif idade == 18:
    print(f'Voce tem {idade} anos, precisa se alistar neste ano!')
else:
    print(f'Voce esta com {idade} anos, isso significa que vc se alistou ha {idade - 18} anos atras.')
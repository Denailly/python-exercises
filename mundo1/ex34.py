salario = float(input('Digite o seu salario: '))

if salario > 1250:
    print(f'Voce recebeu um aumento de 10%, o valor final do seu novo salario eh de:\nR${salario + (salario * 0.1):.2f}')
else:
    print(f'Voce recebeu um aumento de 15%, o valor final do seu novo salario eh de:\nR${salario + (salario * 0.15):.2f}')
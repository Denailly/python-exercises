valor_casa = float(input('Qual eh o valor da casa que deseja comprar? '))
salario_usuario = float(input('Qual eh o seu salario atual? '))
tempo = int(input('Em quantos anos ira pagar a casa? ')) * 12
prestacao_mensal = valor_casa / tempo
limite = salario_usuario * 30 / 100


if prestacao_mensal <= limite:
    print('Parabéns! Você pode comprar a casa.')
else:
    print('Infelizmente, você não pode comprar a casa. A prestação é muito alta.')

print(f'Prestação mensal: R$ {prestacao_mensal:.2f}')
print(f'Limite permitido: R$ {limite:.2f}')
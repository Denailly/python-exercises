import random

valor_produto = round(random.uniform(0.99, 299.99), 2)
print(valor_produto)

print('Qual sera a forma de pagamento?')
print('1 - Dinheiro ou Cheque | A vista')
print('2 - Cartao')
metodo_pagamento = int(input())

if metodo_pagamento == 1:
    print(f'10% de desconto')
    print(f'Valor do produto: {valor_produto:.2f}')
    print(f'Valor com desconto: {valor_produto - (valor_produto * (10 / 100)):.2f}')
elif metodo_pagamento == 2:
    print('A vista ou parcelado?')
    print('1 - A vista')
    print('2 - Parcelado')
    tipo_pagamento = int(input())
    if tipo_pagamento == 1:
        print(f'Valor do produto: {valor_produto:.2f} 5% de Desconto')
        print(f'Valor com desconto: {valor_produto - (valor_produto * (5 / 100)):.2f}')
    elif tipo_pagamento == 2:
        print('Ate 2x sem juros!')
        qtd_parcelas = int(input('Digite a quantidade de parcelas: '))
        if qtd_parcelas == 1:
            print(f'Valor do produto: {valor_produto:.2f} 5% de Desconto')
            print(f'Valor com desconto: {valor_produto - (valor_produto * (5 / 100)):.2f}')
        elif qtd_parcelas > 1 and qtd_parcelas <= 2:
            print(f'Valor do produto: {valor_produto:.2f}')
            print(f'Total a pagar: {valor_produto:.2f}')
        else:    
            print(f'Valor parcelado em {qtd_parcelas}x: {valor_produto:.2f}')
            print(f'20% de juros')
            print(f'Total com Juros: {valor_produto + (valor_produto * (20 / 100)):.2f}')
else:
    print('Metodo de pagamento invalido, tente novamente')
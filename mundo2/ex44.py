import random

valor_produto = round(random.uniform(0.99, 299.99), 2)
print(valor_produto)

print('Qual sera a forma de pagamento?')
print('1 - A vista | Dinheiro ou Cheque | 10% Desconto')
print('2 - A vista | Cartao | 5% Desconto')
print('3 - Ate 2x | Cartao | Sem Juros')
print('4 - 3x ou mais | Cartao | 20% Juros')

metodo_pagamento = int(input())

if metodo_pagamento == 1:
    print(f'Valor do produto: {valor_produto:.2f}')
    print(f'Valor com desconto: {valor_produto - (valor_produto * (10 / 100)):.2f}')
elif metodo_pagamento == 2:
    print(f'Valor do produto: {valor_produto:.2f}')
    print(f'Valor com desconto: {valor_produto - (valor_produto * (5 / 100)):.2f}')
elif metodo_pagamento == 3:
    print(f'Valor do produto: {valor_produto:.2f}')
    print(f'Total a pagar: {valor_produto:.2f}')
elif metodo_pagamento == 4:
    qtd_parcelas = input(f'Em quantas vezes deseja parcelar: ')
    print(f'Valor parcelado em {qtd_parcelas}x: {valor_produto:.2f}')
    print(f'Total com Juros: {valor_produto + (valor_produto * (20 / 100)):.2f}')
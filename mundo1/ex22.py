nome = str('Danilo Costa')

print(f'Nome com todas as letras minusculas: {nome.lower()}')
print(f'Nome com todas as letras maiusculas: {nome.upper()}')
print(f'Quantas letras sem espacos: {len(nome.replace(' ', ''))}')

array_nome = nome.split()
print(f'Quantas letras tem o primeiro nome: {len(array_nome[0])}')
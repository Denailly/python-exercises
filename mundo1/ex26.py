frase = 'arara azul'
frase = frase.upper()

print(f'Tamanho da frase: {len(frase)} letras')
print(f'Quantos A temos na frase: {frase.count('A')}')
print(f'Onde a primeira letra A aparece: {frase.find('A') + 1}')
print(f'Onde a ultima letra A aparece: {frase.rfind('A') + 1}')

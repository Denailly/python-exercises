n1 = 12
n2 = 9
n3 = 11

maior = n1
menor = n1

if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

print(f'O maior numero eh {maior} e o menor numero eh {menor}')
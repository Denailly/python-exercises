pesos = []

for x in range(1, 6):
    pesos.append(float(input(f'digite o peso da {x} pessoa: ')))
print(pesos)

print(f'Maior peso = {max(pesos)}')
print(f'Menor peso = {min(pesos)}')


# FORMA MAIS SIMPLES
# maior = 0
# menor = 0

# for x in range(1,6):
#     peso = float(input(f'Digite o peso da {x} pessoa = '))

#     if x == 1:
#         maior = peso
#         menor = peso

#     if peso < menor:
#         menor = peso
#     elif peso > maior:
#         maior = peso

# print()
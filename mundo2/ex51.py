# 10 TERMOS DE UMA PROGRESSAO ARITMETICA

termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))
decimo_termo = termo + (10 - 1) * razao

print(f'Primeiro termo: {termo}')
print(f'Razao: {razao}')

for c in range(termo, decimo_termo + razao, razao):
    print(f'{c}', end=' -> ')
print(f'FINISH')
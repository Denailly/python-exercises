soma = int(0)

for c in range(0, 6):
    valor_digitado = int(input('Digite um valor a somar: '))
    if valor_digitado % 2 == 0:
        soma += valor_digitado
print(soma)
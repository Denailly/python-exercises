valor = []

for c in range(0, 6 ):
    valor.append(int(input('Digite um numero: ')))

# Para cada numero dentro do array VALOR, ele adiciona o numero em NUM se o valor for divisivel por 2
soma = sum(num for num in valor if num % 2 == 0)

print(soma)
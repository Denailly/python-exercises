peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso / (altura ** 2)

print(f'IMC = {imc:.2f}')

if imc <= 18.5:
    print(f'IMC = {imc:.2f}\nAbaixo do Peso')
elif 18.5 < imc <= 25:
    print(f'IMC = {imc:.2f}\nPeso Ideal')
elif 25 < imc <= 30:
    print(f'IMC = {imc:.2f}\nSobrepeso')
elif 30 < imc <= 40:
    print(f'IMC = {imc:.2f}\nObesidade')
else:
    print(f'IMC = {imc:.2f}\nObesidade morbida')
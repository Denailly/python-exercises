n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

if n1 == n2:
    print(f'os valores {n1} e {n2} sao iguais, nenhum eh maior! =)')
elif n1 > n2:
    print(f'O primeiro valor eh maior que o segundo! {n1} > {n2}')
else:
    print(f'O segundo valor eh maior que o primeiro! {n2} > {n1}')

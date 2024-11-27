numero = int(input('Digite um numero: '))
opcao = int(input('digite: \n1 - Binario\n2 - Octal\n3 - Hexadecimal'))

if opcao == 1:
    print(f'O numero {numero} em binario: {bin(numero)[2:]}')
elif opcao == 2:
    print(f'O numero {numero} em octal: {oct(numero)[2:]}')
elif opcao == 3:
    print(f'O numero {numero} em Hexadecimal: {hex(numero)[2:]}')
else:
    print('Opcao invalida! Tente novamente.')

print(f'Obrigado!')
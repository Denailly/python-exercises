# Numero primo

n = int(input('Digite um numero para saber se ele eh um numero primo: '))
verify_prime = 0

for c in range(0, n+1):
    if n % c == 0:
        verify_prime += 1


if verify_prime == 2:
    print(f'{n} eh um numero primo!') 
else:
    print(f'{n} NAO eh um numero primo!')
from random import randint

n1 = randint(1,10)
n2 = randint(1,10)
n3 = randint(1,10)


print(f'lado 1 = {n1}')
print(f'lado 2 = {n2}')
print(f'lado 3 = {n3}')

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('eh possivel fazer um triangulo :)')

    if n1 == n2 == n3:
        print(f'Equilatero')
    elif (n1 == n2 and n1 != n3) or (n3 == n2 and n3 != n1) or (n3 == n1 and n3 != n2):
        print(f'Isosceles')
    elif n1 != n2 and n2 != n3 and n3 != n1:
        print(f'Escaleno')
        
else:
    print('nao eh possivel fazer um triangulo')
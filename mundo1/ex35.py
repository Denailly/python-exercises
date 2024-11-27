from random import randint

n1 = randint(1,30)
n2 = randint(1,30)
n3 = randint(1,30)

print(f'lado 1 = {n1}')
print(f'lado 2 = {n2}')
print(f'lado 3 = {n3}')

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('eh possivel fazer um triangulo :)')
else:
    print('nao eh possivel fazer um triangulo')
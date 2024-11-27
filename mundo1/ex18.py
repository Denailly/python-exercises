import math

angulo = float(input('Digite um angulo: '))

sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tg = math.tan(math.radians(angulo))

print(f'sen = {sen:.2f}\ncos = {cos:.2f}\ntg = {tg:.2f}')
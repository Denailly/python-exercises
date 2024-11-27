# Crie um programa
# que leia um numero
# Real qualquer pelo
# teclado a mostra na
# tala a sua porsao
# Inteira.

# Ex:
# Digite um numero: 6.127
# 0 numcro 6.127 tem a
# parte Intcira 6.

import math
import random
n1 = random.uniform(0, 999)

print(f'Parte inteira de {n1} é {math.trunc(n1)}')
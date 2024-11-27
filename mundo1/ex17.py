import math
import random

co = random.uniform(0, 999)
ca = random.uniform(0, 999)

h = math.hypot(ca, co)

print(f'o valor de h baseado em =>\n Cateto oposto: {co:.2f}m\n Cateto adjacente: {ca:.2f}m\n\n hipotenusa: {h:.2f}m')
# Soma de todos os numeros NATURAIS divisiveis por 4 e 8
# Naturais = 0 a 250

# NUMEROS NATURAIS

s = 0
for numero_nat in range(0, 250 + 1):
    if numero_nat % 4 == 0 and numero_nat % 8 == 0:
        print(numero_nat)
        s += numero_nat
print(s)
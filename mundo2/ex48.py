s = 0
for numero in range(1, 500+1):
    if numero % 3 == 0 and numero % 2 == 1:
        s += numero
print(s)
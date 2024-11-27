n1 = float(input('digite sua primeira nota: '))
n2 = float(input('digite sua segunda nota: '))

media = round((n1 + n2) / 2, 1)

if media < 5.0:
    print(f'media: {media} - REPROVADO')
elif media >= 5.0 and media <= 6.9:
    print(f'media: {media} - RECUPERACAO')
else:
    print(f'media: {media} - APROVADO')
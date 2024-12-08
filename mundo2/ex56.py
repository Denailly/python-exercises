homem_mais_velho = str('')
idade_homem_mais_velho = int(0)
qtde_mulheres_menores_20 = int(0)

idade_media = int(0)

for x in range(1,5):
    print(f'=== {x} Pessoa ===')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    genero = str(input('Genero (M/F): '.upper()))

    idade_media += idade

    if x == 1 and genero == 'M':
        homem_mais_velho = nome
        idade_homem_mais_velho = idade
    
    if genero == 'M' and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        homem_mais_velho = nome

    if genero == 'F' and idade < 20:
        qtde_mulheres_menores_20 += 1

idade_media = idade_media / 4

print(f'A idade media de todas as pessoas eh: {idade_media}')
print(f'Homem mais velho: {homem_mais_velho}, com {idade_homem_mais_velho} anos.')
print(f'A quantidade de mulheres abaixo de 20 anos eh: {qtde_mulheres_menores_20}')
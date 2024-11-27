# Palíndromos

# recebe um input, retira os espaços em branco
# transforma em array, separando cada palavra
frase = str(input('Digite uma frase para verificar se eh um palindromo: ')).strip().upper().split()

# pega cada palavra do array $frase e adiciona a uma string (sem espaços em branco)
junto = ''.join(frase)

# inicia uma string vazia
inverso = ''

# para cada letra entre o range do final da palavra até o inicio da palavra, contando de forma reversa
# ex: ONIBUS = len - 6
# termina de contar apos o range 0, ou seja, -1
# conta de forma regressiva = -1

# adiciona à string $inverso, a letra da variavel $junto no indice da contagem de $letra
# range = 6
# letra = S
# 
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

print(f'termo = {junto}\ninverso = {inverso}')

if inverso == junto:
    print(f'Palíndromo!')
else:
    print('Não é um palíndromo.')
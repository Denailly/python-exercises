from random import randint

velocidade_carro = randint(40, 120)

if velocidade_carro <= 80 :
    print(f'O seu veiculo passou no radar a {velocidade_carro}Km/h, parabens por respeitar as leis de transito!')
else:
    velocidade_excedente = velocidade_carro - 80
    print(f'Voce passou no radar a {velocidade_carro}Km/h, {velocidade_excedente}Km/h a mais do permitido!!!')
    print(f'Por isso, ira pagar uma multa equivalente a R${float(velocidade_excedente * 7):.2f}')
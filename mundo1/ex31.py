distancia_percorrida = float(input('Digite em KM a distancia da sua viagem: '))

if distancia_percorrida <= 200:
    print(f'O valor da sua passagem ficou R${(distancia_percorrida * 0.50):.2f}')
else:
    print(f'O valor da sua viagem acima de 200Km ficou R${(distancia_percorrida * 0.45):.2f}')
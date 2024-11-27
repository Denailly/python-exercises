distancia = float(
    input('Digite a quantidade de KM percorrida com o veiculo: '))

dias = float(input('Quantos dias voce utilizou o veiculo? '))

valor_gasosa = float(0.15)

v_diaria = dias*60
v_gasosa = distancia*valor_gasosa

print(f'Valor de diaria: R${v_diaria:.2f} \nValor por KM rodado: R${v_gasosa:.2f}\n')
print(f'O falor total a pagar pelo aluguel e a gasosa fica: R${(v_gasosa + v_diaria):.2f}')
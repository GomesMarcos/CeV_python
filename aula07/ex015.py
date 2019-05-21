# DESAFIO 15
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dias = int(input('Informe quantos dias o carro ficou alugado: '))
km = float(input('Informe quantos quantos Km o carro rodou: '))
valorDia = 60 * dias
valorKm = .15 * km
total = valorDia + valorKm
print('O total a ser pago pelo aluguel do carro é de: R${:.2f}:\nR${:.2f} pelos dias e R${:.2f} pela quilometragem'.format(total, valorDia, valorKm))
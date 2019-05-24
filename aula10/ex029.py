# Indique a velocidade de um carro. > 80Km/h é multa de 7 conto por km ultrapassado!
vel = int(input('Indique a velocidade do carro: '))
multa = (vel - 90) * 7
if vel > 80 and vel < 90:
    print('Sua multa te aguarda, sacana!')
elif vel > 90:
    print('Sua multa de R${:.2f} te aguarda, sacana!'.format(multa))
else:
    print('Tudo ok.')

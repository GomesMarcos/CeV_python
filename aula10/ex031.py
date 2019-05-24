# Ler a distância de uma viagem e cobrar R$0.50 por Km para viagens até 200Km ou R$0.45 para viagens maiores.
km = float(input('Informe a distância de sua viagem em quilômetros: '))
if km <= 200:
    print('Sua viagem custará: R${}'.format(km*.5))
else:
    print('Sua viagem custará: R${}'.format(km*.45))

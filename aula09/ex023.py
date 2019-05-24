# Leia um número de 0 a 9999 e mostre cada dígito separadamente
# Ex: 1234
# Unidade: 4
# Dezena: 3
# Centena: 2
# Milhar: 1

numero = int(input('Informe um número de 0 a 9999: '))
tamanho = len(str(numero))
if tamanho == 1:
    print('Unidade: {}'.format(numero))

elif tamanho == 2:
    print('Dezena: {}'.format(str(numero)[0]))
    print('Unidade: {}'.format(str(numero)[1]))

elif tamanho == 3:
    print('Centena: {}'.format(str(numero)[0]))
    print('Dezena: {}'.format(str(numero)[1]))
    print('Unidade: {}'.format(str(numero)[2]))

elif tamanho == 4:
    print('Milhar: {}'.format(str(numero)[0]))
    print('Centena: {}'.format(str(numero)[1]))
    print('Dezena: {}'.format(str(numero)[2]))
    print('Unidade: {}'.format(str(numero)[3]))
else:
    print('\'{}\' não está entre 0 e 9999'.format(numero))

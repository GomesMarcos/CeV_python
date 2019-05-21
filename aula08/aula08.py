# Utilizando Módulos
# Módulo matemático
'''
import math # Importação que abrange TODO o módulo
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
quadrado = math.pow(num,2)
print('As operações realizadas com o número {} foram:'.format(num))
print('Raiz quadrada: {}'.format(raiz))
print('Raiz quadrada aproximada pra cima: {}'.format(math.ceil(raiz)))
print('Raiz quadrada aproximada pra baixo: {}'.format(math.floor(raiz)))
print('Potenciação ao quadrado: {}'.format(quadrado))


from math import sqrt, floor, ceil, pow #Importação específica do módulo
raiz = sqrt(num)
quadrado = pow(num,2)
print('Utilizando importação específica:')
print('As operações realizadas com o número {} foram:'.format(num))
print('Raiz quadrada: {}'.format(raiz))
print('Raiz quadrada aproximada pra cima: {}'.format(ceil(raiz)))
print('Raiz quadrada aproximada pra baixo: {}'.format(floor(raiz)))
print('Potenciação ao quadrado: {}'.format(quadrado))
'''

import random
num = random.random()
numInt = random.randint(1,10)
print('Float randômico: {}'.format(num))
print('Int randômico: {}'.format(numInt))


'''
Algumas bibliografias:
Pacotes built-in: https://docs.python.org/3.7/library/index.html
Índice de Pacotes Extras: https://pypi.org/
'''

import emoji
print(emoji.emojize('Olá, mundo!!  :sunglasses:', use_aliases=True))
print(emoji.emojize('Olá, mundo!!  :earth_americas:', use_aliases=True))
# Imprimir a parte inteira de um número float (Consultar https://docs.python.org/3/library/math.html)
from random import random
from math import floor

rand = random()
num = floor(rand * 10)
print('O número {} aproximado para inteiro é: {}'.format(rand, num))
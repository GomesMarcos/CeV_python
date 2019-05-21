#Digitar um ângulo e obter seno e cosseno (Consultar https://docs.python.org/3/library/math.html)
from math import sin, cos

ang = float(input('Informe um ângulo: '))
print('Seu seno é: {} e seu cosseno é: {}'.format(sin(ang), cos(ang)))
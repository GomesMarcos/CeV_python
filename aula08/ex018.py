#Digitar um ângulo e obter seno e cosseno (Consultar https://docs.python.org/3/library/math.html)
from math import sin, cos, tan, radians

ang = float(input('Informe um ângulo: '))
radang = radians(ang)
print('O seno de {:.2f} é: {:.2f}\nSeu cosseno é: {:.2f}\nA tangente é {:.2f}'.format(ang, sin(radang), cos(radang), tan(radang)))
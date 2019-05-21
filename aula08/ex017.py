# ler o cumprimento oposto e o adjascente de um triânngulo retângulo,
# calculando a hipotenusa (Consultar https://docs.python.org/3/library/math.html)
from math import pow, sqrt

cat1 = float(input('Informe um cateto: '))
cat2 = float(input('Informe outro cateto: '))
hip = sqrt(pow(cat1,2) + pow(cat2 , 2))

print(hip)
#ler o nome dos alunos de forma randômica (Consultar https://docs.python.org/3/library/math.html)
from random import shuffle
alunos = ['alberto', 'bigail', 'claudionílson', 'demócrites']
shuffle(alunos)
print('A ordem de apresentação será: {}'.format(alunos))

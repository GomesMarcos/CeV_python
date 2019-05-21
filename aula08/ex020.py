#ler o nome dos alunos de forma randômica (Consultar https://docs.python.org/3/library/math.html)
from random import sample
alunos = ['alberto', 'bigail', 'claudionílson', 'demócrites']

print('Quem vai apagar o quadro será: {}'.format(sample(alunos, len(alunos))))

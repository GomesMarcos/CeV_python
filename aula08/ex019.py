#sortear um dos alunos para apagar o quadro (Consultar https://docs.python.org/3/library/math.html)
from random import choice
alunos = ['alberto', 'bigail', 'claudionílson', 'demócrites']
print('Quem vai apagar o quadro será: {}'.format(choice(alunos)))
#sortear um dos alunos para apagar o quadro (Consultar https://docs.python.org/3/library/math.html)
from random import randint
alunos = ['alberto', 'brianni', 'claudionílson', 'demócrites']
print('Quem vai apagar o quadro será: {}'.format(alunos[randint(0, len(alunos) -1)]))
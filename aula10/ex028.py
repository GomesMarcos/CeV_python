# gere um número randômico entre 0 e 5 e, se o usuário digitar o correto, ele vence.
from random import randint
r = randint(0, 5)
while True:
    num = int(
        input('Selecione um número entre 0 e 5. Para finalzar digite \'000\': '))

    if num == 000:
        print('-=-' * 5 + 'Finalizando programa' + '-=-' * 5)
        break
    elif num == r:
        print('Acetô!! Miserávi!! {}'.format(r))
        print('-=-' * 5 + 'Finalizando programa' + '-=-' * 5)
        break

    else:
        print('Errrrrroooou!')

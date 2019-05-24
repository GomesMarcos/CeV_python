# Leia um número informado e diga se é um ano bisexto
ano = int(input('Informe um ano: '))
if ano % 4 == 0:
    print('{} é um ano bissexto'.format(ano))
else:
    print('{} não é um ano bissexto'.format(ano))

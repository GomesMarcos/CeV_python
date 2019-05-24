# Leia uma frase qualquer e informe:
# quantas vezes aparece a letra 'a',
# em qual índice ela aparece pela primeira vez
# Em qual índice ela aparece pela última vez

frase = input('Informe uma frase: ')

print('\'' + frase + '\' possui {} letras'.format(len(frase)))
print('A letra \'a\' aparece {} vezes'.format(frase.count('a')))
print('A letra \'a\' aparece pela primeira vez na posição: {}'.format(frase.find('a')))
print('A letra \'a\' aparece pela última vez na posição: {}'.format(frase.rfind('a')))

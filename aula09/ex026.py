# Leia uma frase qualquer e informe:
# quantas vezes aparece a letra 'a',
# em qual índice ela aparece pela primeira vez
# Em qual índice ela aparece pela última vez

frase = str(input('Informe uma frase: ')).strip().upper()

print('\'' + frase + '\' possui {} letras'.format(len(frase)))
print('A letra \'a\' aparece {} vezes'.format(frase.count('A')))
print('A letra \'a\' aparece pela primeira vez na posição: {}'.format(frase.find('A')+1))
print('A letra \'a\' aparece pela última vez na posição: {}'.format(frase.rfind('A')+1))

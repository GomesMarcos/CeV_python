# Estruturas condicionais
'''tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3 and tempo > 0:
    print('{} anos?! Novinho ainda!!'.format(tempo))
else:
    print('{} anos?! Já tá na hora, em?!'.format(tempo))
# print('Novinho ainda!!' if tempo <= 3 else'Já tá na hora, em?!')
print('--FIM--')
'''

### PRÁTICA ###
'''nome = str(input('Qual seu nome? '))

if nome == 'Murilo':
    print('Mesmo nome do meu filho!!! *_*')
else:
    print('Seu nome é bem comum, em?')
print('Bom dia, {}!'.format(nome))
'''

###
n1 = float(input('Digite uma nota: '))
n2 = float(input('Digite outra nota: '))
media = (n1 + n2) / 2

if media >= 5:
    print('Passou com média {:.1f}. Miserávi!'.format(media))
else:
    print('Perdeu com média {:.1f}. Silascou!'.format(media))

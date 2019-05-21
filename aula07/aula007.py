# ====AULA 07====
nome = input('Qual o seu nome? ')
print('Muito prazer, {:<20}!! (Alinhado à esquerda em 20 caracteres)'.format(nome))
print('Muito prazer, {:^20}!! (Alinhado ao centro em 20 caracteres)'.format(nome))
print('Muito prazer, {:>20}!! (Alinhado à direita em 20 caracteres)'.format(nome))
print('Muito prazer, {:=^20}!! (Alinhado ao centro, preenchido com \'=\' em 20 caracteres)'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
print('A soma vale: {} \n'.format(n1+n2), end=' ')
print('A subtração vale: {}\n'.format(n1-n2), end=' ')
print('A potenciação vale: {} \n'.format(n1**n2), end=' ')
print('O resto da divisão vale: {}'.format(n1//n2))

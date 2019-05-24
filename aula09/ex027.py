# Leia o nome completo de uma pessoa e mostre o 1º e último nome separadamente
# Ex: Ana Maria Mattos Souza
# Primeiro Nome: Ana
# Última Nome: Souza

nome = input('Digite seu nome: ')
print('Seu primeiro nome é: {}'.format(nome.split()[0]))
print('Seu último nome é: {}'.format(nome.split()[-1]))

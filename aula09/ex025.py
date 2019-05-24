# Leia o nome completo de uma pessoa e identifique se ela possui "Silva" no nome
nome = input('Informe seu nome completo: ')
nome = nome.split()
if 'Silva' in nome:
    print('Seu nome possui \'Silva\'')
else:
    print('Seu nome não possui \'Silva\'')

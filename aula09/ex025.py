# Leia o nome completo de uma pessoa e identifique se ela possui "Silva" no nome
nome = str(input('Informe seu nome completo: ')).strip()
if 'SILVA' in nome.upper():
    print('Seu nome possui \'Silva\'!')
else:
    print('Seu nome não possui \'Silva\'!')

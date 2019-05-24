# Ler o nome completo de uma pessoa e:
# printar o nome com todas as letras maiúsculas
# printar o nome com todas as letras minúsculas
# printar quantas letras ao todo (sem considerar os espaços)
# printar quantas letras tem o primeiro nome

nome = input('Informe seu nome completo: ')
print('Nome em maiúsculo: {}'.format(nome.upper()))
print('Nome em minúsculo: {}'.format(nome.lower()))
nomeSplit = nome.split()
nomeSplit = ''.join(nomeSplit)
print('Quantidade de letras: {}'.format(len(nome)))
print('Quantidade de letras sem contar espaços: {}'.format(len(nomeSplit)))
print('Quantidade de letras no primeiro nome: {}'.format(len(nome.split()[0])))

# Leia 3 cumprimentos de retas e informe se eles podem formar um triângulo
r1 = float(input('Iinforme o cumprimento da 1ª reta: '))
r2 = float(input('Iinforme o cumprimento da 2ª reta: '))
r3 = float(input('Iinforme o cumprimento da 3ª reta: '))

if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('É possivel montar um triângulo com as retas de cumprimento {}, {} e {}'.format(r1, r2, r3))
else:
    print('Não é possivel montar um triângulo com as retas de cumprimento {}, {} e {}'.format(r1, r2, r3))

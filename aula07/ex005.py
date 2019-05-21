num = int(input('Digite um número: '))
antecessorNum = num-1
sucessorNum = num+1
dobroNum = num*2
triploNum = num*3
raizQNum = pow(num,1/2)
print('Seu antecessor é: {}. Seu sucessor é: {}'.format(antecessorNum, sucessorNum))
print('Seu dobro é: {}. Seu triplo é: {}. Sua raiz quadrada é: {}'.format(dobroNum, triploNum, raizQNum))

# DESAFIO 07
nota1 = float(input('Informe sua primeira nota: '))
nota2 = float(input('Informe sua segunda nota: '))
media = (nota1 + nota2) / 2
print('A sua média foi: {:.1f}'.format(media))

# DESAFIO 08
medida = float(input('Informe uma medida em Metro: '))
centimetros = medida * 100
milimetros = centimetros * 10
print('{}m = {}cm = {}mm'.format(medida, centimetros, milimetros))

# DESAFIO 09
taboada = int(input('Informe um número inteiro para formar sua taboada: '))
i = 1
print('-' * 12)
while i < 11:
  print('{} x  {:2} = {}'.format(taboada, i, (taboada * i)))
  i += 1
print('-' * 12)

# DESAFIO 10
dinheiroEmReal = float(input('Quantos reais você tem na carteira? R$'))
dinheiroEmDolar = dinheiroEmReal / 4.1
print('Você possui: U${:.2f}.'.format(dinheiroEmDolar))

# DESAFIO 11
alturaParede = float(input('Informe a altura de uma parede a ser pintada: '))
larguraParede = float(input('Informe a largura de uma parede a ser pintada: '))
area = alturaParede * larguraParede
litros = area/2
print('Sabendo que cada lata de tinta pintam 2m² de parede, para pintar uma parede de {}m² serão necessárias {}l de tinta'.format(area, litros))

# DESAFIO 12
preco = float(input('Quanto custa esse produto: R$'))
preco95 = preco * .95

print('A vista ele sai por: R${:.2f}'.format(preco95))

# DESAFIO 13
salarioBase = float(input('Meu salário antigo era de: R$'))
salarioAtual = salarioBase * 1.15
print('Agora ganho 15% a mais. Ou seja: R${:.2f}'.format(salarioAtual))

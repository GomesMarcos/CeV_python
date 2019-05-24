# Leia um salário e, se for igual ou maior a 1250 o aumento é de 10%, menor que isso, o aumento é de 15%.
s = float(input('Informe o seu salário: R$'))

if s <= 1250:
    print('Seu aumento é de 15%. O novo salário é: R${:.2f}'.format(s*1.15))
else:
    print('Seu aumento é de 10%. O novo salário é: R${:.2f}'.format(s*1.1))

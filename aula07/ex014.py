# DESAFIO 14
celsius = float(input('Informe uma temperarura em Celsius: '))
far = (celsius * 9/5) + 32
kelvin = celsius + 273
print('A temperatura {:.1f}ºC em Fahrenheit é de {:.1f}ºF e {}ºK'.format(celsius, far, kelvin))
# 05:10 - Fatiamento de String;
# 13:50 - Análise:
# 14:15 - len();
# 14:50 - count();
# 16:35 - find();
# 18:55 - in;
# 19:35 - Transformação:
# 19:55 - replace();
# 20:50 - upper();
# 21:50 - lower();
# 22:25 - capitalize();
# 23:04 - title();
# 24:34 - strip();
# 25:08 - rtrip();
# 25:50 - lstrip();
# 26:35 - Divisão:
# 26:50 - split();
# 28:20 - Junção:
# 28:35 - join();

frase = 'Curso em Vídeo Python'

# Fatiamento
'''print(frase[9]) # Fatiamento: letra única
print(frase[9:14]) # Fatiamento: substring
print(frase[9:21]) # Fatiamento: substring maior
print(frase[9:21:2]) # Fatiamento: substring pulando de 2 em 2
print(frase[:5]) # Fatiamento: substring do início até o índice 5
print(frase[15:]) # Fatiamento: substring do índice 15 até o final
print(frase[9::3]) # Fatiamento: substring do índice 9 até o final, pulando de 3 em 3'''

# Análise
print(len(frase))  # Tamanho da string
print(frase.count('o'))  # Quantas vezes aparece o char 'o'
# Quantas vezes aparece o char 'o' entre o índice 0 a 12
print(frase.count('o', 0, 13))
print(frase.find('deo'))  # Em qual índice aparece a substring 'deo'
print(frase.find('Android'))  # Substring inexistente retorna o valor -1
print('Curso' in frase)  # Verifica se a substring existe na string (True/False)

# Transformação
# Substitui a primeira substring pela segunda
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
# Analisa quantas palavras a string possui e torna a primeira letra de cada maiúscula
print(frase.title())

frase = '   Aprenda Python  '
print(frase.strip())  # Remove os espaços no início e no final da string
print(frase.rstrip())  # Remove os espaços direita da string
print(frase.lstrip())  # Remove os espaços na esquerda da string

# Divisão
frase = 'Curso em Vídeo Python'
# Divide a string, tendo como parâmetro padrão os espaços entre as letras,
print(frase.split())
# em uma lista de seus "pedaços" a partir dos espaços
frase = frase.split()
print('.'.join(frase))  # Adiciona o caractere '.' entre cada índice da string

############PRÁTICA DA AULA 09################
frase = 'Curso em Vídeo Python'
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[1::2])
print(frase[::2])
print("""
MACETE!!!
Curso em Vídeo Android
CURSO EM VÍDEO PYTHON
curso em vídeo python
Curso em vídeo python
Curso Em Vídeo Python
Aprenda Python
""")

print(frase.count('o'))
print(frase.count('O'))
print(len(frase))
frase = """
MACETE!!!
Curso em Vídeo Android
CURSO EM VÍDEO PYTHON
curso em vídeo python
Curso em vídeo python
Curso Em Vídeo Python
Aprenda Python
"""
print(len(frase))

frase = 'Curso em Vídeo Python'
print(frase.replace('Python', 'Android'))
print(frase[0])
print('Curso' in frase)
print(frase.find('Curso'))

print(frase.lower().find('vídeo'))
dividido = frase.split()
print(dividido[0])
print(dividido[2][3])
print(dividido[2].find('d'))

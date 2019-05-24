# Leia o input do nome de uma cidade e verifique se ela começa com a palavra "Santo"
cidade = str(input('Informe sua cidade: ')).strip()
cidade = cidade.split()
if cidade[0].capitalize() == 'Santo':
    print('Sua cidade começa com Santo!')
else:
    print('Sua cidade não começa com \'Santo\'!')

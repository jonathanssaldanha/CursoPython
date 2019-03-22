tempo = int(input('Quantos anos tem seu carro?'))
if tempo <=3:
    print('Seu carro é considerado novo')
else:
    print('Seu carro é considerado velho')


print('\nCarro novo' if tempo <= 3 else 'Carro velho')

nome = str(input('Qual é seu nome? '))
if nome == 'Jonathan':
    print('\nQue nome lindo você tem!')
else:
    print('\nSeu nome é tao normal!')
print('Bom dia, {}!'.format(nome))

print('----FIM----')
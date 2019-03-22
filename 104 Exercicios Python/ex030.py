num = int(input('Digite um numero: '))
resultado = num % 2
print('O resto da divisao foi : {}'.format(resultado))
if resultado == 1:
    print('O numero é IMPAR')
else:
    print('O numero é PAR')
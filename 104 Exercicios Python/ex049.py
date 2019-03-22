# REFAÇA O DESAFIO 009, MOSTRANDO QUE O USUARIO ESCOLHER, SO QUE AGORA UTILIZANDO UM LAFO FOR

num = int(input('Digite um numero para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))

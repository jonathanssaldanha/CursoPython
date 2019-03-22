from random import randint
from time import sleep
print('=#=' * 20)
print('VOU PENSAR EM UM NUMERO ENTE 0 E 5. TENTE ADIVINHAR...')
print('=#=' * 20)
computador = randint(0, 5)  # faz o computador pensar/sortead
jogador = int(input('\nEm que numero eu pensei? '))  # jogador tenta adivinhar
print('CARREGANDO...')
sleep(3)
if jogador == computador:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no numero {} e não no {}'.format(computador, jogador))

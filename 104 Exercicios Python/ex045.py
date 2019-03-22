# CRIAR UM PRAGRAMA QUE FAÇA O COMPUTADOR JOGAR JOKENPO COM VC

from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual sua jogada? '))
print('\033[33mJO')                 #   \033[33m   > apartir daqui tudo fica nessa for ate encontrar   # >  \033[m
sleep(1)
print('\033[33mKEN')
sleep(1)
print('\033[33mPO!!!')
print('\033[m-='*20)                # Fim da cor > \033[m
print('O computador jogou {}'.format(itens[computador]))
print('Jogador      jogou {}'.format(itens[jogador]))
print('-='*20)
if computador == 0:         # computador jogou pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador Venceu')
    elif jogador == 2:
        print('Computador Venceu')
    else:
        print('JOGADA INVALIDA')
elif computador == 1:       # computador jogou pedra
    if jogador == 0:
        print('Computador Venceu')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador Venceu')
    else:
        print('JOGADA INVALIDA')
elif computador == 2:       # computador jogou pedra
    if jogador == 0:
        print('Jogador Venceu')
    elif jogador == 1:
        print('Computador Venceu')
    elif jogador == 2:
        print('Empate')
    else:
        print('JOGADA INVALIDA')

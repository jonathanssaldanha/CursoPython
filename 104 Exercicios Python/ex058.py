# MELHORE O JOGO DO DESAFIO 028 ONDE O COMPUTADOR VAI 'PENSAR' EM UM NUMERO ENTRE 0 E 10. SO QUE
# AGORA O JOGADOR VAI TENTAR ADIVINHAR ATE ACERTAR, MOSTRANDO NO FINAL
# QUANTOS PALPITES FORAM NECESSARIOS PARA VENCER

from random import randint
computador = randint(0, 10)
print('Sou seu computador... \nAcabei de penar em um numero entre 0 e 10.')
print('Sera que voce consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} palpites, Parabens'.format(palpites))

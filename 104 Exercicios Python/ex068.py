# faça um programa que jogue par ou impar com o computador.
# o jogo so sera interrompido quano o jogador perder, mostrando
# o total de vitorias consecutivas que ele conquistou no final do jogo.

from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I]: ')).strip().upper()
        print('='*20)
    print(f'Voce jogou {jogador} e o computador {computador}. total de {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('\033[0;32mVoce Venceu!\033[m')
            v += 1
        else:
            print('\033[0;32mVoce Perdeu!\033[m')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('\033[0;32mVoce Venceu!\033[m')
            v += 1
        else:
            print('\033[0;32mVoce Perdeu!\033[m')
            break
    print('=' * 20)
    print('Vamos jogar novamente...')
print('='*20)
print(f'GAME OVER! Voce venceu {v} vezes')
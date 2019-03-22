# CRIE UM PROGRAMA QUE LEIA UMA FRASE QUALQUER E DIGA SE ELA É UM PALINDROMO,
# DESCONSIDERANDO OS ESPAÇOS.
# exemplos     APOS A SOPA  |   A SACADA DA CASA    |   A TORRE DA DERROTA  |   O LOBO AMA O BOLO
#              ANOTARAM A DATA DA MARATONA

frase = str(input('Digite uma frase qualquer: ')).strip().upper()
palavras = frase.split()
print('Você digitou a frase {}'.format(frase))
print('Você digitou a frase {}'.format(palavras))
junto = ''.join(palavras)
print('Você digitou a frase {}'.format(junto))
inverso = ''
inverso= junto[::-1]        # substitui o for
'''for letra in range(len(junto)-1, -1, -1):   # 1° = começa a onde? na ultima letra
                                               # 2° = vai para onde?  ate a primeira letra na posiçao 0 = -1
                                               # 3° = +1 para andar para frente e -1 para andar para tras
    inverso += junto[letra]
'''
print('O inverso de {} é {}'.format(junto, inverso))
print('\n')
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('NÁO É Palindromo!')

# ESCREVA UM PROGRAMA QUE LEIA UM NUMERO N INTEIRO
# QUALQUER E MOSTRE NA TELA OS N PRIMEIROS
# ELEMENTOS DE UMA SEQUENCIA DE FIBONACCI
#EX
# 0 > 1 > 1 > 2 > 3 > 5 > 8

print('-' * 30)
print('Sequencia de Fibonacci')
print('-' * 30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('-'*30)
print('{} > {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' > {}'.format(t3), end='')
    t1 = t2     # passa o valor de t2 para t1 para andar uma posicao para frente
    t2 = t3     # passa o valor de t3 para t2 para andar uma posicao para frente
    cont += 1   # muda o valor do contador de 1 em 1
print(' > Fim')
print('-'*30)

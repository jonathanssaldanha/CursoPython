# CRIE UM PROGRAMA QUE LEIA VARIOS NUMEROS INTEIROS
# PELO TECLADO. O PROGRAMA SO VAI PARAR QUANDO O USUARIO
# DIGITAR O VALOR 999, QUE É A CONDIÇÃO DE PARADA. NO FINAL,
# MOSTRE QUANTOS NUMEROS FORAM DIGITADOS E QUAL FOI A SOMA
# ENTRE ELS( DESCONSIDERANDO O FLAG.

#-------------------while com condiçao de parada----------#
n = 1
cont = soma = 0
while n != 999:
    n = int(input('Digite um valor ou (99 para parar): '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'A soma dos {cont} valores é {soma}')
print('Fim')
print('='*20)

#--------------------Loping infinito----------------------#
soma = cont = 0
while True:
    num = int(input('Digite um valor ou ( 999 para parar ): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} valores foi {soma}')
print('Fim')

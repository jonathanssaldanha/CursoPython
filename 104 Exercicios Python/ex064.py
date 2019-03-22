# CRIE UM PROGRAMA QUE LEIA VARIOS NUMEROS INTEIROS PELO TECLADO.
# O PROGRAMA SO VAI PARAR QUANDO O USUARIO DIGITAR O VALOR 999,
# QUE É A CONDIÇAO DE PARADA. NO FINAL, MOSTRE QUANTOS NUMEROS
# FORAM DIGITADOS E QUAL FOI A SOMA ENTRE ELES(DESCONSIDERANDO O FLAG)

num = cont = soma = 0
num = int(input('Digite um valor: [999 para parar]: ')) # tecnica para nao contar ou somar o valor da condicao de saida
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um valor: [999 para parar]: '))
print('-' * 30)
print('Voce digitou {} numeros.'.format(cont))
print('A soma dos valores foi {}.'.format(soma))
print('-' * 30)
print('Fim')
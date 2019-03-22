# ex065.py
# CRIE UM PROGRAMA QUE LEIA VARIOS NUMEROS INTEIROS PELO TECLADO.
# NO FINAL DA EXECUÇÃO, MOSTRE A MEDIA ENTRE TODOS OS VALORES
# E QUAL FOI O MAIOR E MENOR VALORES LIDOS. O PROGRAMA DEVE
# PERGUNTAR AO USUARIO SE ELE QUER OU NAO CONTINUAR A DIGITAR VALORES.

soma = media = cont = maior = menor = 0
resp = 'S'
while resp in 'Ss':
    num = int(input('Digite um valor: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
media = soma / cont
print('Voce digitou {} numero e a sua media foi {}'.format(cont, media))
print('A soma dos valores doi {}'.format(soma))
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
print('Fim')
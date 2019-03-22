# CRIE UM PROGRAMA QUE LEIA DOIS VALORES E MOSTRE UM MENU COMO AO LADO NA TELA:
# SEU PROGRAMA DEVERA REALIZAR A OPERAÇÃO SOLICITADA EM CADA CASO.

#[1] - SOMAR
#[2] - MULTIPLICAR
#[3] - MAIOR
#[4] - NOVOS NUMEROS
#[5] - SAIR DO PROGRAMA

from time import sleep
n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
opcao = 0
while opcao != 5:
    print('''    [1] - Somar
    [2] - Multiplicação
    [3] - Maior
    [4] - Maior
    [5] - Sair do programa''')
    opcao = int(input('>>>>>Qual é a sua opção? '))
    if opcao == 1:      # Somar
        soma = n1 + n2
        print('A Soma entre {} + {} é: {}'.format(n1, n2, soma))
    elif opcao == 2:      # Multiplicaçao
        multiplicacao = n1 * n2
        print('A multiplicaçao de {} x {} é: {}'.format(n1, n2, multiplicacao))
    elif opcao == 3:      # Maior
        if n1 > n2:
            maior = n1
            print('O maior numero digitado foi: {} '.format(maior))
        else:
            maior = n2
            print('O maior numero digitado foi: {}'.format(maior))
    elif opcao == 4:      # Novos Numeros
        print('Informe os numeros novamente')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor:'))
    elif opcao == 5:      # Sair
        print('Finalizando...')
    else:
        print('Opçao invalida. tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa, volte sempre')

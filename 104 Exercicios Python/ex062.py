# MELHORE O DESAFIO 061, PERGUNTANDO PARA O USUARIO SE ELE
# QUER MOSTRAR MAIS ALGUNS TERMOS, O PROGRAMA ENCERRA
# QUANDO ELE DISSER QUE QUER MOSTRAR 0 TERMOS

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro: '))
razao = int(input('Razao da Pa: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} > '.format(termo), end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos voce quer mostrar a mais? '))
print('Progressao finalizada com {} termos mostrados'.format(total))
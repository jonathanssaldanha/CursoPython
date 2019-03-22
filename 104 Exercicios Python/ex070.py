# CRIE UM PROGRAMA QUE LEIA O NOME E O PREÇO DE VARIOS PRODUTOS.
# O PROGRAMA DEVERA PERGUNTAR SE O USUARIO VAI CONTINUAR. NO FINAL MOSTRE:
# A) QUAL É O TOTAL GASTO NA COMPRA
# B) QUANTOS PRODUTOS CUSTAM MAIS DE R$ 1000,00
# C) QUAL É O NOME DO PRODUTO MAIS BARATO.

total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$ '))
    cont += 1
    total += preço

    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    #else:                              ESSE BLOCO SE REPETE, E POR ISSO FOI POSTO EM UMA LINHA, OTIMIZAÇÃO NO CODIGO
    #    if preço < menor:
    #        menor = preço
    #        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('Fim do Programa'))
print(f'O total da compra foi R$ {total:10.2f}')
print(f'Temos {totmil} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi >> {barato} que custa R$ {menor:.2f}')
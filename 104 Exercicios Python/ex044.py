# ELABORE UM PROGRAMA QUE CALCULE O VALOR A SER PAGO POR UM PRODUTO, CONSIDERANDO
# O SEU PREÇO NORMAL E CONDIÇÃO DE PAGAMENTO:
# - À VISTA DINHEIRO / CHEQUE COM 10% DESCONTO          - EM ATE 2X NO CARTAO: PREÇO NORMAL
# - À VISTA NO CARTÃO: 5% DESCONTO                      - 3X OU MAIS NO CARTÃO: 20% DE JUROS

print('{:=^40}'.format(' Loja Jonathan '))
preco= float(input('Preco das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] Á vista dinheiro / cheque
[ 2 ] À vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual o opção: '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f}'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalparc = int(input('Quantas parcelas: '))
    parcela = total / totalparc
    print('Sua compra sera em {}x de R$ {:.2f} com juros'.format(totalparc, parcela))
else:
    total = preco
    print('Opção invalida de pagamento. tente novamente')
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final '.format(preco, total))

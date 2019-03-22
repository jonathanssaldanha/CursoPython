casa = float(input('Valor da casa: R$ '))
salario = float(input('Salario do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
minimo = salario * 30 / 100
# IMPRESSAO DAS SAIDAS
print('\nPara pagar uma casa de R$ {:.2f} em {} anos,'.format(casa, anos), end='') # end para juntar a sua linha a linha de baixo
print(' a prestação sera de R$ {:.2f}'.format(prestação))
# condiçao 30 percento do salario
if prestação <= minimo:
    print('Emprestimo pode ser CONCEDIDO!')
else:
    print('Emprestimo NEGADO!')

#teste 01
#print('Comparando tem que pagar R$ {} e o minimo é de R$ {}'.format(prestação,minimo))
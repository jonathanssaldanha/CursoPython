preco = float(input('Digite o valor do produto: R$ '))
desconto5 = (preco * 15 / 100)
saldo = preco - desconto5

print('O valor do produto R$ {:.2f}, com desconto de 15% fica R$ {:.2f} Reais.'.format(preco, saldo))
print('O valor do produto R$ {:.2f}, com desconto de 15% fica R$ {:.2f} Reais.'.format(preco, preco-(preco * 15 / 100)))


distancia = float(input('Digite quantos quilometros a viagem: '))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

# metodo simplificado de fazer a mesma coisa ( operador ternario: açao/ condiçao/ açao )
# preco = distancia * 0.50 is distancia <= 200 else distancia * 0.45

print('e o preço da sua passagem sera de R$ {:.2f} '.format(preco))


altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))

area = altura * largura
quant_Tinta = area / 2

print('\nA parede possui uma area de {} metros quadrados.'.format(area))
print('A parede possui {} metros de altura por {} de largura, e precisa de {} litros de tinta para pintar a parede.'.format(altura, largura, quant_Tinta))

print('\nA parede possui uma area de {} metros quadrados.'.format(altura*largura))
print('A parede possui {} metros de altura por {} de largura, e precida de {} litros de tinta para pintar a parede.'.format(altura, largura, (altura*largura)/2))
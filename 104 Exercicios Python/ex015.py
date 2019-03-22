dias = float(input('Informe dias alugados: '))
km = float(input('Informe Km rodados: '))
valorCarroDia = 60.00
valorKm = 0.15
pago = (dias * valorCarroDia) + (km * valorKm)

print('Total a pagar: R$ {:.2f} '.format(pago))


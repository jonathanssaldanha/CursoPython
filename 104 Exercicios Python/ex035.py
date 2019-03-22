print('-='*20)
print('Analisando de tringulos')
print('-='*20)
r1 = float(input('Digite um valor: '))
r2 = float(input('Digite um valor: '))
r3 = float(input('Digite um valor: '))
# A soma de dois lados tem que ser maior que 1 elenento. testar todos os elementos um a um.
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos a cima PODEM formar um TRIANGULO.')
else:
    print('Os seguimentos a cima NAO PODEM formar um TRIANGULO.')
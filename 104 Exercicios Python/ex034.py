salario = float(input('Digite o valor do seu salario: R$ '))

if salario <= 1250:
    newsalario = salario + (salario * 15 / 100)
else:
    newsalario = salario + (salario * 10 / 100)
print('Quem ganhava R$ {:.2f} passa a ganhar R$ {:.2f} agora.'.format(salario, newsalario))
salario = float(input('Digite o valor do salario: '))
aumento = salario * 1.15
inss = salario * 8 / 100
fgts = salario * 8 / 100
ferias33 = salario * 33 / 100
addNoturno = salario * 20 / 100
cestaBasica = 18
print('O salario do funcionario é R$ {:.2f} reais e com o aumento de 15% ficou R$ {:.2f} Reais.'.format(salario, aumento))
print('O salario do funcionario é R$ {:.2f} Reais e com o aumento de 15% ficou R$ {:.2f} Reais.'.format(salario, salario * 1.15))

print('\nAdicional noturno: R$ {:.2f}'.format(addNoturno))

print('\nCesta Basica: R$ {:.2f} '.format(cestaBasica))
print('Fgts: R$ {:.2f}'.format(fgts))
print('INSS: R$ {:.2f}'.format(inss))
print('1/3 das ferias: R$ {:.2f}'.format(ferias33))

valorbruto = salario
valorliquido = (salario + addNoturno + ferias33) - (fgts + inss + cestaBasica)

print('\nValor bruto a receber: R$ {:.2f}'.format(valorbruto))
print('Valor Liquido a receber : R$ {:.2f}'.format(valorliquido))
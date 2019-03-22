# entrada de dados
nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))
salario = int(input('Digite seu salario: '))
mesesTrabalhado = int(input('Meses trabalhados: '))

# condiçao inss
if salario <= 998:
    inss = salario * 8 / 100
if salario > 998 and salario <= 1560:
    inss = salario * 9 / 100
if salario > 1560 and salario <= 2350:
    inss = salario * 10 / 100
elif salario > 2350:
    inss = salario * 11 / 100

# condição fgts
if salario <= 998:
    fgts = salario * 8 / 100
if salario > 998 and salario <= 1560:
    fgts = salario * 9 / 100
if salario > 1560 and salario <= 2350:
    fgts = salario * 10 / 100
elif salario > 2350:
    fgts = salario * 11 / 100

#decimo 13°
decimo13 = salario * mesesTrabalhado / 12

# condiçao ferias 33%
ferias33 = salario * 33 / 100

#calcular as entradas menos as saidas
liquido = (salario + ferias33) - (fgts + inss)

# saida de dados
print(f'O {nome:-^20} tem {idade} anos e ganha R${salario}.')  # Python 3.6+
print(f'Inss: {inss:.2f}')
print(f'Fgts: {fgts:.2f}')
print(f'Ferias 33% : {ferias33:.2f}')
print(f'Salario Liquido: {liquido}')
print(f'Decimo 13° : {decimo13:.2f}')
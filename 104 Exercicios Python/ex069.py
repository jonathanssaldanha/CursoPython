# CRIE UM PROGRAMA QUE LEIA A IDADE E O SEXO DE VARIAS PESSOAS.
# A CADA PESSOA CADASTRADA, O PROGRAMA DEVERA PERGUNTAR SE O USUSARIO QUER OU NAO CONTINUAR. NO FINAL MOSTRE.
# A) QUANTAS PESSOAS TEM MAIS DE 18 ANOS.
# B) QUANTOS HOMENS FORAM CADASTRADOS.
# C) QUANTAS MULHERES TEM MENOS DE 20 ANOS.

tot18 = totH = totM20 = 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('='*20)
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homes cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')
print('Acabou')
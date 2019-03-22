# A CONFEDEREÇÃO NACIONAL DE NATAÇÃO PRECISA DE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO
# DE UM ATLETA E MOSTRE SUA CATEGORIA, DE ACORDO COM IDADE:
# ATE  9 ANOS: MIRIM      ATE 19 ANOS: JUNIOR
# ATE 14 ANOS: INFANTIL   ATE 25 ANOS: SENIOR
#                         ACIMA: MASTER

from datetime import date
atual = date.today().year
nascimento= int(input('Ano nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:                              # Menor igual a 9
    print('Classificação: MIRIM')
elif idade <= 14:                     # IGUAL  >>> IDADE > 9 AND IDADE <= 14
    print('Classificação: INFANTIL')
elif idade <= 19:                     # IGUAL  >>> IDADE > 14 AND IDADE <= 19
    print('Classificação: JUNIOR')
elif idade <= 25:                     # IGUAL  >>> IDADE > 19 AND IDADE <= 25
    print('Classificação: SENIOR')
else:                          # Maior igual a 25
    print('Classificação: MASTER')
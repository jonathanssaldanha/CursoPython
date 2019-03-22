# FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORME, DE ACORDO COM SUA IDADE,
# SE ELE AINDA VAI SE ALISTAR AO SERVIÇO MILITAR, SE É A HORA DE SE ALISTAR OU SE JÁ PASSOU O TEMPO DO ALISTAMENT.
# SEU PROGRAMA TAMBÉM DEVERA MOSTRAR O TEMPO QUE FALTA OU QUE PASSOU DO PRAZO

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade= atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade <18:
    saldo = 18 - idade
    print('Ainda falta {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade -18
    print('Você deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
# CRIE UM PROGRAMA QUE SIMULE O FUNCIONAMENTO DE UM CAIXA ELETRONICO.
# NO INICIO, PERGUNTE AO USUARIO QUAL SERA O VALOR A SER SOCADO (NUMERO INTEIRO)
# E O PROGRAMA VAI INFORMAR QUANTAS CEDULAS DE CADA VALOR SERAO ENTREGUES
# OBS: CONSIDERE QUA A CAIXA POSSUI CEDULAS DE R$ 50,00 / R$ 20,00 / R$ 10,00 / R$ 1,00

print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Que valor voce quer sacar? R$ '))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd        # VALOR - CED (50 REAIS)
        totcéd += 1        # QUANTAS VEZES EU CONSGIDO TIRAR 50 DO TOTAL
    else:                   #SE NAO DER PARA TIRAR 50 REAIS DO TOTAL
        if totcéd > 0:      # SO IMPRIMIR SE O NUMERO DE NOTAS FOR MAIOR QUE ZERO
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:       # SE O VALOR FOR MENOR QUE 50
            céd = 20
        elif céd == 20:     # SE O VALOR FOR MENOR QUE 20
            céd = 10
        elif céd == 10:        # SE O VALOR FOR MENOR 10
            céd = 1
        totcéd = 0
        if total == 0:
            break
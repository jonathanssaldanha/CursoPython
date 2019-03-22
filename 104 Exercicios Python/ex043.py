# DESENVOLVA UMA LOGICA QUE LEIA O PESO E A ALTURA DE UMA PESSOA.
# CALCULE O IMC E MOSTRE SEU STATUS, DE ACORDO COM A TABELA ABAIXO
# ABAIXO DE 18.5: ABAIXO DO PESO     25 ATE 30 : SOBREPESO
# ENTRE 18.5 E 25: PESO IDEAL        30 ATE 40: OBESIDADE
#                                    ACIMA DE 40: OBESIDADE MÓRBIDA

peso = float(input('Qual o seu peso? (Kg): '))
altura = float(input('Qual é sua altura? (M): '))
imc = peso / (altura **2)
print('O IMC dessa pessoa é de {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:      # imc >= 18.5 and imc < 25
    print('Você está no PESO IDEAL')
elif 25 <= imc < 30:
    print('Você está com SOBREPESO')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE, cuidado!')
elif imc >= 40:
    print('Você está em OBESIDADE MORBIDA, cuidado!')
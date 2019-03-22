# REFAÇA O DESAFIO 35 DOS TRIANGULOS, ACRESCENTANDO O RECURSO DE
# MOSTRAR QUE TIPO DE TRIANGULO SERA FORMADO:
# EQUILATERO: TODOS OS LADOS IGUAIS
# ISOSCELES: DOIS LADOS IGUAIS
# ESCALENO: TODOS OS LADOS DIFERENTES

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triangulo!')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos acima NAO PODEM FORMAR triangulo')
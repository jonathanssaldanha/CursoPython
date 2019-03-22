#import math
from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))

#usamos um tipo de variavel que ja temos no modulo padrao, sem importação
print('O valor digitado foi {} e a sua porção inteiro é {}'.format(num, int(num)))
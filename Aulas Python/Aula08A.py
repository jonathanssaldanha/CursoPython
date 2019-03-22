import math
#from math import sqrt, floor -> para importar um Método destinto e não a biblioteca toda
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)

print('\nA raiz quadrada de {} é igual {:.2f} arredonda pra cima'.format(num, math.ceil(raiz)))
print('A raiz quadrada de {} é igual {:.2f} raiz quadrada sem usar variavel'.format(num, math.sqrt(num)))
print('A raiz quadrada de {} é igual {:.2f} arredonda para baixo'.format(num, math.floor(raiz)))
print('A raiz quadrada de {} é igual {:.2f} pega o valor da variavel raiz'.format(num, raiz))

#print('fatorial de {} é igual {}'.format(num, math.factorial(num)))

import random
bh = random.random()    #essa função sorteia um numero entre 0 e 1
print('\n{}'.format(bh))
bc = random.randint(1, 10)# essa funçao sortei um numero entre (x, y)
print('{}'.format(bc))

import emoji
print(emoji.emojize("Olá, Mundo :sunglasses:", use_aliases=True))
print(emoji.emojize("Olá, Mundo :football:", use_aliases=True))
print(emoji.emojize("Olá, Mundo :hamburger:", use_aliases=True))
print(emoji.emojize("Olá, Mundo :fuelpump:", use_aliases=True))
print(emoji.emojize("Olá, Mundo :arrow_double_up:", use_aliases=True))
print(emoji.emojize("Olá, Mundo :underage:", use_aliases=True))
print(emoji.emojize("Olá, Mundo :bangbang:", use_aliases=True))
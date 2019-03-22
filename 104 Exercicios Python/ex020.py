# exemplo de ordem de apresentaçao de trabalho na faculdade
from random import shuffle
print('========Programa recebe uma lista, embaralha esse lista e devolve a impressao na ordem embaralhada======')
aluno01 = str(input('Nome do primeiro aluno: '))
aluno02 = str(input('Nome do segundo aluno: '))
aluno03 = str(input('Nome do terceiro aluno: '))
aluno04 = str(input('Nome do quarto aluno: '))
lista = [aluno01, aluno02, aluno03, aluno04]
#shuffle => embaralhar(lista)
shuffle(lista)
print('\nA ordem de apresentação sera: ')
print(lista)

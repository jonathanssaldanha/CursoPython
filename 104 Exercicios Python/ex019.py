from random import choice
print('=====================Programa que sortea um nome para fazer algo===================')
aluno01 = str(input('Primeiro aluno: '))
aluno02 = str(input('Segundo aluno: '))
aluno03 = str(input('Terceiro aluno: '))
aluno04 = str(input('Quarto aluno: '))
lista= [aluno01, aluno02, aluno03, aluno04]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
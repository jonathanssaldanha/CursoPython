# CODIGO DAS CORES [STYLE][TEXT][BACKGROUND]
print('\033[0;30mOlá, Mundo!\033[m')
print('\033[1;30mOlá, Mundo!\033[m')
print('\033[4;30mOlá, Mundo!\033[m')
print('\033[7;30mOlá, Mundo!\033[m')
print('\033[7;30;46mOlá, Mundo!\033[m') # METODO COM OS TRES TERMOS 7;30;46

print('\033[1;31mOlá, Mundo!\033[m')
print('\033[4;31mOlá, Mundo!\033[m')
print('\033[4;31mOlá, Mundo!\033[m')
print('\033[7;31mOlá, Mundo!\033[m')

print('\033[0;32mOlá, Mundo!\033[m')
print('\033[1;32mOlá, Mundo!\033[m')
print('\033[4;32mOlá, Mundo!\033[m')
print('\033[7;32mOlá, Mundo!\033[m')

print('\033[0;33mOlá, Mundo!\033[m')

# metodo de cores numero 01 / COM OS CODIGO DENTRO DO PRINT
print('-' * 30)
nome = 'Jonathan'
idade = 27
sexo = 'Masculino'
print('Olá! Muito prazer em te conhecer, {}{}{}'.format('\033[4;31m', nome, '\033[m'))
print('A sua idade é : {}{}{}'.format('\033[0;31m', idade, '\033[m'))
sobrenome = 'Saldanha'
print('Sexo: {}{}{}'.format('\033[0;31m', 'sexo', '\033[m'))

# metodo de cores numero 02 / COM AS CORES DENTRO DE UMA VARIAVEL CORES
print('-' * 30)
nome = 'Saldanha'
idade = 28
sexo = 'Masculino'
cores = {'limpa': '\033[m', 'azul': '\033[34m', 'amarelo': '\033[33m', 'pretoebranco': '\033[7;30m'}
print('Ola, muito prazer em te conhecer, {}{}{}'.format(cores['azul'], nome, cores['limpa']))
print('A sua idade é: {}{}{}'.format(cores['azul'], idade, cores['limpa']))
print('Sexo: {}{}{}'.format(cores['azul'], sexo, cores['limpa']))
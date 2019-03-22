nome = input('Qual é seu nome? ')
print('Prazer em te conhecer: {:>20}!'.format(nome))
print('Prazer em te conhecer: {:<20}!'.format(nome))
print('Prazer em te conhecer: {:^20}!'.format(nome))
print('Prazer em te conhecer: {:=^20}!'.format(nome))


n1 = int(input('\nUm valor: '))
n2 = int(input('Outro valor: '))
soma = n1 + n2
multi = n1 * n2
div = n1 // n2
exp = n1 ** n2
print('\nA soma entre {} e {} vale {}'.format(n1, n2, soma))
print('A soma entre {} e {} vale {}'.format(n1, n2, (n1+n2)))
print('A multiplicação entre {} e {} vale {}'.format(n1, n2, multi))
print('A divisão entre {} e {} vale {:.3f}'.format(n1, n2, div))
print('O valor {} no expoente {} vale {}'.format(n1, n2, exp))

print('\nA soma é {}, \nO produto é {} e a divisão é {:.3f},'.format(soma, multi, div), end='>>> ')
print('Divisão inteira {} e \npotencia {}'.format(div, exp))

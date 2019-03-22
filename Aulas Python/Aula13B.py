s = 0
for c in range(1, 3+1):
    n = int(input('Digite um valor: '))
    print('A posição {} da tabela tem o valor {} armazenado'.format(c, n))
    s += n
print('='*20)
print('A soma dos valores é {}'.format(s))
print('='*20)
print('Fim')


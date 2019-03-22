for c in range(1, 7):           # sequencia do for 1/2/3/4/5/6
    print('{} - Oi'.format(c))
print('Fim')
print('='*20)

for c in range(6, 0, -1):   # oque o menos 1 faz : 6-1 / 5-1 / 4-1 ...
    print(c)
print('Fim')
print('='*20)

n = int(input('Digite um numero: '))
for c in range(0, n):
    print(c)
print('Fim')

i = int(input("Inicio: "))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):  # significa : inicio ate o fim pulando de 1 em 1 / (F+1) para mostrar a quantidade correta de repetições, o python por padrao nao conta a ultima repetição
    print(c)
print('Fim')



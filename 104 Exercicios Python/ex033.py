a = int(input('Primeiro numero: '))
b = int(input('Segundo numero: '))
c = int(input('Terceiro numero: '))

# Verificando quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

# Verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

# imprimir o numero menor e maior
print('O MENOR valor digitado foi {}'.format(menor))
print('O MAIOR valor digitado foi {}'.format(maior))

##########              EXEMPLO 01             ##########################
'''for c in range(1, 10):
    print(c)
print('Fim')'''

c = 1
while c < 10+1: # imprimi do numero 1 ao 10
    print(c)
    c = c +1
print('Fim')
print('='*20)
##########              EXEMPLO 02             ##########################
'''for c in range(1, 3+1):
    n = int(input('Digite um valor: '))
print('Fim')'''

n = 1
while n != 0:
    n = int(input('Digite um valor ou zero para sair: ')) # condição zero para parar
print('Fim')
print('='*20)
##########              EXEMPLO 03             ##########################
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Deseja continuar? [S/N] : ')).upper()
print('Fim')
##########              EXEMPLO 04             ##########################
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor ou zero para sair: '))
    if n!= 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Voce digitou {} numeros pares e {} numeros impares '.format(par, impar))
print("Fim")
##########              EXEMPLO 05             ##########################
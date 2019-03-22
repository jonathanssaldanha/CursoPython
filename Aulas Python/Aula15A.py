# imprimir
num = int(input('quantos numeros quer mostrar : '))
cont = 1
while cont <= num:
    print(cont, ' -> ', end='')
    cont += 1
print('Fim')
print('='*20)

#somando os valores digitados dentro do luping ate a condiçao de parada
n = s = 0
while True:             # Luping infinito
        n = int(input('Digite um valor ou [ 999 para parar ] '))
        if n == 999:
            break
        s += n
#print('A soma vale {}'.format(s))
print(f'A soma vale {s}')       # usando as F strings
print('Fim')
print('='*20)

# entrada de dados
nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))
salario = int(input('Digite seu salario: '))

#condiçao inss
if salario <= 998:
    inss = salario * 8 / 100
if salario > 998 and salario <= 1560:
    inss = salario * 9 / 100
if salario > 1560 and salario <= 2350:
    inss = salario * 10 / 100
elif salario > 2350:
    inss = salario * 11 / 100

#condição fgts

# saida de dados
print(f'O {nome:-^20} tem {idade} anos e ganha R${salario}.')            #Python 3.6+
print('O {} tem {} anos.'.format(nome, idade))  #Python 3.0
print('O %s tem %d anos.' % (nome, idade))      #Python 2.0
print(f'Inss: {inss:.2f}')
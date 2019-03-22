# REFAÇA O DESAFIU 051, LENDO O PRIMEIRO TERMO E A RAZAO
# DE UMA PA, MOSTRANDO OS 10 PRIMEIROS TERMOS DA
# PROGRESSAO USANDO A ESTRUTURA WHILE

print('Gerador de PA')
print('-='*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao da Pa: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} > ' .format(termo), end='')
    termo += razao
    cont += 1
print('FIM')
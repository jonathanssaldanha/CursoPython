#   FAÇA UM PROGRAMA QUE CALCULE A SOMA ENTRE TODOS OS NUMEROS IMPARES QUE SAO MULTIPLUS DE
#   TRES E QUE SE ENCONTRAM NO INTERVALO DE 1 ATE 500

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c% 3 == 0:
         cont += 1                               #cont = cont + 1
         soma += c                               #soma = soma + c
                                                 #print(c, end=' ')
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))

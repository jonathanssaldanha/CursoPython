#   DESENVOLVA UM PROGRAMA QUE LEIA SEIS NUMEROS INTEIROS E MOSTRE A SOMA
#   AGENAS DAQUELES QUE FOREM PARES, SE O VALOR DIGITADO FOR IMPAR, DESCONSIDERE-O.

soma = 0
cont = 0
for c in range(1, 6):
    num = int(input("Digite o {} valor: ".format(c)))
    soma += num
    cont += 1
print("Você informou {} numeros e a soma foi {}". format(cont, soma))

soma = 0
cont = 0
for c in range(1, 6):
    if num % 2 == 0:
        soma += num
        cont += 1
print("Você informou {} numeros PARES e a soma foi {}". format(cont, soma))

soma = 0
cont = 0
for c in range(1, 6):
    if num % 3 == 0:
        soma += num
        cont += 1
print("Você informou {} numeros IMPAR e a soma foi {}". format(cont, soma))
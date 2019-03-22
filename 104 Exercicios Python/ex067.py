# FAÇA UM PROGRAMA QUE MOSTRE A TABUADA DE VARIOS NUMEROS,
# UM DE CADA VEZ, PARA CADA VALOR DIGITADO PELO USUARIO. O
# PROGRAMA SERA INTERROMPIDO QUANDO O NUMERO SOLICITADO FOR
# NEGATIVO.


while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*20)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-'*20)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')

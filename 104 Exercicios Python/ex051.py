#   DESENVOLVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZAO DE UMA PA. NO FINAL,
#   MOSTRE OS 10 PRIMEIRO TERMOS DESSA PROGRESSÃO

primeiro = int(input("Primeiro termo: "))
razao = int(input('Razao: '))
decímo = primeiro + (10 - 1) * razao            # FORMULA PARA MOSTRAR OS 10 PRIMEIROS TERMOS DESSE PROGRAMA
for c in range(primeiro, decímo + razao, razao):               #  for c in range(1, 10, 1):
    print('{} '.format(c), end=' > ')
print('Acabou')
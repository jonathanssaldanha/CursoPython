#FAÇA UM PROGRAMA QUE LEIA O SEXO DE UMA PESSOA, MAS SO ACEITE
#OS VALORES 'M' OU 'F'. CASO ESTEJA ERRADO, PEÇA A DIGITAÇÃO
#NOOVAMENTE ATE TER UM VALOR CORRETO

sexo = str(input('Digite seu sexo  [M/F] : ')).strip().upper()[0]   # [0] para pegar a primeira letra da palavra que foi digitada
while sexo not in 'MF':
    sexo = str(input('Dados invalidos. por fabor , informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
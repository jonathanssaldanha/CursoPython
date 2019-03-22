# CRIE UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO E CALCULE SUA MEDIA.
# MOSTRANDO UMA MENSAGEM NO FINAL , DE ACORDO COM A MEDIA ATINGIDA;
# MEDIA ABAIXO DE 5.0: REPROVADO
# MEDIA ENTRE 5.0 E 6.9: RECUPERAÇÃO
# MEDIA 7.0 OU SUPERIOR: APROVADO

nota1 = float(input('primeira nota: '))
nota2 = float(input('segunda nota: '))
media = (nota1 + nota2) / 2
print('A media entre a nota {:.1f} e {:.1f} é {:.1f}'.format(nota1, nota2, media))
if 7 > media >= 5:                      # IGUAL A >>>>  media >= 5 and media < 7
    print('O aluno esta em RECUPERAÇÃO')
elif media < 5:
    print('O aluno esta REPROVADO')
elif media >= 7:
    print('O aluno esta APROVADO')
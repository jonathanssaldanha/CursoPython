nota1= float(input('Digite a primeira nota:'))
nota2= float(input('Digite a segunda nota: '))
media= (nota1+nota2)/2
print('A media foi {:.2f}'.format(media))


if media > 6:
    print('Aprovado')
else:
    print('Reprovado')
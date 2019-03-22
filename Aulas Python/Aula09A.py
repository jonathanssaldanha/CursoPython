frase = 'Curso em Video Python'
print(frase)
print(frase[:18])
print(frase[0:15])
print(frase[5:13])
print(frase[::2])   # inicio : fim : pulando de 2 em 2

print('A letra (o) aparece {} vezes nesta frase'.format(frase.count('o')))

print('A letra (o) aparece {} vezes nesta frase'.format(frase.upper().count('O')))  # upper muda tudo para maiuscula , cont conta todas as letras que sao semelhantes a especificada nos parenteses



print('A letra (d) aparece {} vezes nesta frase'.format(frase.count('d')))

print(frase.upper())  # coloca todas as letras em maiuscula

print(frase.replace('Python','Android')) # substitui a palavrade origem pela nova e altera a quantidade de caracteres na frase

print('Qual o tamanha da frase : {} casas decimais'.format(len(frase)))

frase = frase.replace('Python','Android')
print(frase)

print('Curso' in frase)     # verifica se tem a palavra curso na frase e retorna True and false
print('Jonathan' in frase)  # verifica se tem a palavra Jonathan na frase e retorna True and false

print(frase.find('Curso'))  # retorna a posição inicial da palavra
print(frase.find('Video'))  # retorna a posição inicial da palavra
print(frase.find('video'))  # nao encontrou nada e retorna -1
print('A letra (o) aparece na poisiao {} '.format(frase.lower().find('o'))) # lower passa toda a frase para minusculo e depois com o (find) retorna a primeira posição em que a letra (o) aparece.

print(frase.split())    # Criou uma lista (tupla) para cada palavra da frase

dividido = frase.split()    # foi criado uma tupla para cada palavra e salvo na variavel/objeto dividido
print(dividido[0])          # estou pedindo para imprimir a primeira tupla do objeto dividido
print(dividido[1])          # estou pedindo para imprimir a segunda tupla do objeto dividido
print(dividido[2])          # estou pedindo para imprimir a terceira tupla do objeto dividido
print(dividido[2][3])       #imprima a letra da 3° posiçao da tupla 2 = ( 0=v 1=i 2=d ( 3=e ) 4=o )
print(dividido[3])          # estou pedindo para imprimir a quarta tupla do objeto dividido
print(dividido[3][:3])      # estou pedindo para imprimir da posiçao 0 ate a 3 da tupla numero 3, (0,1,2,/3) lembrando que nao pego a posiçao 3 e sim ate a posição 3.
print(dividido[3][1:4])     # estou pedindo para imprimir da posiçao 1 ate a 4 da tupla numero 3


print("""\nWelcome! Are you completely new to programming?
abaut why and how to get started with Python. Fortunately 
an experienced programmer in any programming language
(Whatever it may be) can pick up Python very quickly.
Its also easy for beginners to use and learn, so junp in!!""")
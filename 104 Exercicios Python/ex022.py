print('=== LEITOR DE NOMES ===')

# Coloquei o sobrenome também, por isso as linhas extras
nome = input('Insira seu nome: ').strip()  # strip ele elimina os espaços antes do inicio e depois do fim da string

letras = len(nome) - nome.count(' ')  # len define o tamanho da string e o cont esta somando o numero espaços
print('Nome em maiúsculo: {}'.format(nome.upper()))
print('Nome em minúsculo: {}'.format(nome.lower()))
print('Número de letras: {}'.format(letras))
print('Número de letras: {}'.format(len(nome) - nome.count(' ')))

dividido = nome.split()  # dividi a string apartir do espaço [jonathan] [saldanha] [de] [jesus]
print('Primeiro nome: {}. Ele tem {} letras'.format(dividido[0], nome.find(' ')))
print('Primeiro nome: {}. Ele tem {} letras'.format(dividido[0], len(dividido[0])))
print('Sobrenome: {}. Ele tem {} letras'.format(' '.join(dividido[1:]), letras - nome.find(' ')))
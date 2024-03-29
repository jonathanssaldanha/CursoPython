print('=== LEITOR DE NÚMEROS ATÉ 9999 ===')
n = int(input('Digite um número até 9999: '))

print('== MÉTODO COM VARIAVEL ==')
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Unidade = {}'.format(u))
print('Dezena = {}'.format(d))
print('Centena = {}'.format(c))
print('Milhar = {}'.format(m))

print('== MÉTODO INT ==')
print('Unidade = {}'.format(n % 10))
print('Dezena = {}'.format((n // 10) % 10))
print('Centena = {}'.format((n // 100) % 10))
print('Milhar = {}'.format(n // 1000))

print('== MÉTODO STRING ==')
n = '000' + str(n)  # para que possamos escrever 1, 23 ou 395
print('Unidade = {}'.format(n[-1]))  # Também daria pra usar n[len(n)-1]
print('Dezena = {}'.format(n[-2]))
print('Centena = {}'.format(n[-3]))
print('Milhar = {}'.format(n[-4]))
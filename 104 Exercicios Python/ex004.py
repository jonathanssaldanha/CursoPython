a = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a))
print('So tem espaços: ', a.isspace())
print('É um numero: ', a.isnumeric())
print('É alfabétivo: ', a.isalpha())
print('É uma alfanumerico: ', a.isalnum())
print('Esta em maiuscula: ', a.isupper())
print('Esta em minuscula: ', a.islower())
print('Esta capitalizada:', a.istitle())
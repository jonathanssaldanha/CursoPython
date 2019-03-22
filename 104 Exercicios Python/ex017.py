
#metodo com importação
import math
catetoOposto = float(input('Comprimento do Cateto Oposto: '))
catetoAdjacente = float(input('Comprimento do Cateto Adjacente: '))
hipotenusa = math.hypot(catetoOposto, catetoAdjacente)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))

##metodo sem importaçao
#catetoOposto = float(input('Comprimento do Cateto Oposto: '))
#catetoAdjacente = float(input('Comprimento do Catetp Adjacente: '))
#hipotenusa = (catetoOposto ** 2 + catetoAdjacente ** 2) ** (1/2)
#print('A Hipotenusa vai medir {:.2f}'.format(hipotenusa))
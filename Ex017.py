import math
catetoOposto = float(input('Comprimento do cateto oposto: '))
catetoAdjacente = float(input('Comprimento do cateto adjacente: '))
print(f'A hipotenusa vai medir {math.hypot(catetoOposto, catetoAdjacente):.2f}')

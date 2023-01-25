metros = float(input('Uma distancia em metros: '))
km = metros / 10 / 10 / 10
hm = metros / 10 / 10
dam = metros / 10
dm = metros * 10
cm = metros * 10 * 10
mm = metros * 10 * 10 * 10
print(f'A media de {metros}m corresponde a {km}km')
print(f'{km}km')
print(f'{hm}hm')
print(f'{dam}dam')
print(f'{dm:.0f}dm')
print(f'{cm:.0f}cm')
print(f'{mm:.0f}mm')

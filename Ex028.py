from random import randint
from time import sleep
print("-="*20)
print('Vou pensar em um numero de 0 . 5 tente advinhar... ')
computador = randint(0, 6)
sleep(3)
jogador = int(input('Em que numero eu pensei? '))
print('Vejamos...')
sleep(3)
if jogador == computador:
    print(f'Parabéns você ganhou! eu pensei no numero {computador}')
else:
    print(f'Tente novamente! eu pensei no numero {computador} e não no numero {jogador}')


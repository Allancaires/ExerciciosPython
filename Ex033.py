maior = menor = 0
numero = int(input('Digite o primeiro valor:'))
numero2 = int(input('Digite o segundo valor:'))
numero3 = int(input('Digite o terceiro valor:'))
def Maior_numero(maior):
    if numero > numero2 and numero > numero3:
        maior = numero
    elif numero2 > numero and numero2 > numero3:
        maior = numero2
    else:
        maior = numero3
    print(f'O maior valor digitado foi {maior}')

def Menor_numero(menor):
    if numero < numero2 and numero < numero3:
        menor = numero
    elif numero2 < numero and numero2 < numero3:
        menor = numero2
    else:
        menor = numero3
    print(f'O menor valor digitado foi {menor}')
Maior_numero(maior)
Menor_numero(menor)


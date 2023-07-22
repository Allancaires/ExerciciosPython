numero = int(input('Escolha um numero para Conversão: '))
usuario = int(input('Escolha a Opção desejada: /n Opção1 Bínario /n Opção2 Octal /n Opção3 Hexadecimal '))
if usuario == 1:
    print(f'O numero {numero} em bínario é {bin(numero)}')
elif usuario == 2:
    print(f'O numero {numero} em Octal é {oct(numero)}')
elif usuario == 3:
    print(f'O numero {numero} em Hexadecimal é {hex(numero)}')
else:
    print('Numero não cadastrado!')

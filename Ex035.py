lado_a = float(input('Qual valor do lado A:'))
lado_b = float(input('Qual valor do lado B:'))
lado_c = float(input('Qual valor do lado C:'))

if lado_a + lado_b > lado_c:
    print('A soma dos valores digitados formam um triangulo!')
elif lado_b + lado_a > lado_c:
    print('A soma dos valores digitados formam um triangulo!')
elif lado_c + lado_b > lado_a:
    print('A soma dos valores digitados formam um triangulo!')
else:
    print('A soma dos valores digitados não formam um triangulo!')

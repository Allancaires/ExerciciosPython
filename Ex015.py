Dias = int(input('Quantos dias de aluguel? '))
KmRodado = int(input('Quantos Km rodados? '))
AluguelDias = Dias * 60
Kmvalor = KmRodado * 0.15
print(f'O valor a pagar é de {AluguelDias + Kmvalor}')

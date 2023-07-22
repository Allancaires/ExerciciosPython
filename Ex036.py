custo_casa = float(input('Valor da Cssa: '))
salario_comprador = float(input('Salario do Comprador: '))
financiamento = int(input('Quantos anos de Financiamento: '))
ano = 12
valor_parcela = custo_casa / (financiamento * ano)
valor_financiamento = salario_comprador * 30 / 100
if valor_financiamento <= valor_parcela:
    print(f'Emprestimo Aprovado!')
    print(f'Para pagar uma Casa no valor de {custo_casa:.2f} a parcela mensal será de {valor_parcela:.2f}')
else:
    print('Seu Financiamento foi Negado! pois sua parcela não pode exceder os 30% do seu salario.')




produto = float(input('Qual o valor do produto? R$ '))
desconto = (produto * 5.0) / 100
print(f'O produto que custava R${produto} na promoção com desconto de 5% vai custar {produto - desconto}')

viagem = int(input('Qual a distancia da sua viagem? '))
if viagem <= 200:
    Valor_viagem = viagem * 0.50
    print(f'Você está prestes a ingressar em uma viagem de {viagem}Km\n no valor de R$: {Valor_viagem:.2f} ')
elif viagem > 200:
    Valor_viagem = viagem * 0.45
    print(f'Você está prestes a ingressar em uma viagem de {viagem}Km\n no valor de R$: {Valor_viagem:.f} ')

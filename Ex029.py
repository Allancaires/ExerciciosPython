velocidade_atual = int(input('Qual a velocidade Maxima do carro? '))
if velocidade_atual > 80:
    multa = (velocidade_atual - 80) * 7.0
    print(f'Você excedeu o limite permitido e será multado no valor de {multa:.2f}')
print('Tenha um Bom dia! Dirija com segurança.')

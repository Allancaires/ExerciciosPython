salario_atual = float(input('Qual o salario do funcionario: '))
aumento_salario = 0
if salario_atual > 1250:
    aumento_salario = (salario_atual * 10) / 100
elif salario_atual < 1250:
    aumento_salario = (salario_atual * 15) / 100
print(f'O funcionario agora recebera o valor de {salario_atual + aumento_salario}')

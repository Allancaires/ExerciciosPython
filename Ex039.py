from _datetime import datetime

ano_nascimento = int(input('Digite sua data de Nascimento: '))
ano_atual = datetime.now().year
idade_alistamento = ano_atual - ano_nascimento

if idade_alistamento == 18:
    print(f'{ano_atual} É seu Ano de alistamento militar! va ate a junta militar mais proxima de você. ')
elif idade_alistamento < 18:
    saldo = 18 - idade_alistamento
    print(f'Ainda Falta {saldo} Anos para seu alistamento militar!')
elif ano_nascimento > 18:
    saldo = idade_alistamento - 18
    print(f'Seu alistamento deveria ter sido feito há {saldo} Anos.')

import datetime
from datetime import date
from time import sleep

ano_atual = datetime.date.today().year
ano_digitado = int(input('Digite o ano a ser analisado: '))
print('Analisando!')
sleep(3)

if ano_digitado % 4 == 0 and ano_digitado % 100 != 0 or ano_digitado % 400 == 0:
    ano_digitado = ano_atual
    print(f' O ano {ano_digitado} é BISEXTO')
else:
    print(f'O ano {ano_digitado} não é BISEXTO')

nome = str(input('Digite o nome do aluno: ')).capitalize()
nota1 = float(input(f'Digite a primeira nota do aluno {nome}: '))
nota2 = float(input(f'Digite a segunda nota do aluno {nome}: '))
media = (nota1 + nota2) / 2
print(f'A media do aluno {nome} é {media} ')
var = input('Digite algo: ')
print(type(var))
print(f'Só tem espaços? {var.isspace()}')
print(f'É um numero? {var.isnumeric()}')
print(f'É alfabetico? {var.isalpha()}')
print(f'É alfanumerico? {var.isalnum()}')
print(f'Está em maiusculo? {var.isupper()}')
print(f'Está em minusculas? {var.islower()}')
print(f'Está capitalizada? {var.istitle()}')
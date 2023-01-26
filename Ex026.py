nome = str(input('Digite uma frase: ')).upper()
print(f'A letra A aparece {nome[0:].count("A") } vezes na frase.')
print(f'A primeira letra A aparece na {nome.find("A") +1} posição.')
print(f'A Ultima letra A aparece na {nome.rfind("A") + 1} posição.')

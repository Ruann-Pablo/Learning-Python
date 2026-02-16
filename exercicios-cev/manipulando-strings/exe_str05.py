nome = str(input('Digite seu nome: ')).strip().title().split()

print(f'Seu primeiro nome: {nome[0]}')
print(f'Seu segundo nome: {nome[-1]}')
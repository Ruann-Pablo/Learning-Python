tupla = (('Camisa', 120), ('Shorts', 80), ('Chapéu', 40), ('Bolsa', 100), ('Tênis', 400))

print('-' * 30)
print(f'{"LISTAGEM DE PREÇOS":^30}')
print('-' * 30)

for prod, preco in tupla:
    print(f'{prod:.<25}R${preco}')
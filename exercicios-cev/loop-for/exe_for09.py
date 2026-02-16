menor_peso = 0
maior_peso = 0

for i in range(1, 6):
    peso = float(input('Digite o peso: '))

    if peso <= 0:
        print('Peso inválido.')
        continue

    if i == 1:
        menor_peso = peso
        maior_peso = peso
    else:
        if peso < menor_peso:
            menor_peso = peso
    
        if peso > maior_peso:
            maior_peso = peso

print(f'O menor peso foi de: {menor_peso}')
print(f'O maior peso foi de: {maior_peso}')
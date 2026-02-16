soma = 0

for i in range(0, 6):
    numeros = int(input('Digite um número: '))

    if numeros % 2 == 1:
        print(f'numero {numeros} desconsiderado')
        continue
    
    soma += numeros

print(f'A soma dos números pares é de: {soma}')

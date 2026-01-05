soma = 0
cont = 0

while True:
    numero = int(input('Digite um número [999 para parar o programa]: '))

    if numero == 999:
        break

    soma += numero
    cont += 1

print(f'O resultado dos {cont} valores somados foi de: {soma}')
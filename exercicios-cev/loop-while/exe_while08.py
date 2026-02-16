num = 0
soma = 0
cont_soma = 0

while num != 999:
    num = int(input('Digite um número [999 para parar o programa]: '))

    if num != 999:
        soma += num
        cont_soma += 1

print(f'Você digitou {cont_soma} números e a soma entre eles foi de: {soma}')


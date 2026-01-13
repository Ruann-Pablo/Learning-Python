lista = []
resposta = ''

while resposta != 'n':
    valor = int(input('Digite um valor: '))

    if valor in lista:
        print('Valor duplicado! Valor não adicionado a lista.')
    else:
        lista.append(valor)

    resposta  = str(input('Quer continuar? [S/N]: ')).strip().lower()

lista.sort()

print(f'Você digitou os valores: {lista}')
lista = []
maior_valor = 0
menor_valor = 0
repete = 0

while repete < 5:
    repete+=1
    resposta =  int(input('Digite um número: '))
    lista.append(resposta)

    if repete == 1:
        maior_valor = resposta
        menor_valor = resposta
    else:
        if resposta > maior_valor:
            maior_valor = resposta
        elif resposta < menor_valor:
            menor_valor = resposta

print(f'Você digitou os valores: {lista}')

print(f'O maior valor digitado foi {maior_valor} nas posições ', end='')
for i, v in enumerate(lista):
    if v == maior_valor:
        print(F'[{i}]', end=', ')

print(f'\nO menor valor digitado foi {menor_valor} nas posições ', end='')
for i, v in enumerate(lista):
    if v == menor_valor:
        print(F'[{i}]', end='. ')
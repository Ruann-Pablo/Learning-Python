num = 0
soma = 0
media = 0
cont = 0
maior_num = 0
menor_num = 0
resposta = ''

while resposta != 'n':
    num = int(input('Digite um número: '))
    resposta = str(input('Deseja continuar [s/n]? Responda: ')).lower().strip()

    if resposta != 's' and resposta != 'n':
        print('Resposta inválida, Tente novamente com respostas sendo apenas "s" para Sim, ou "n" para "Não".')
        continue

    soma += num
    cont += 1

    if cont == 1:
        maior_num = num
        menor_num = num
    else:
        if num > maior_num:
            maior_num = num
        
        if num < menor_num:
            menor_num = num

media = soma / cont

print(f'A média dos {cont} números digitados foi de: {media}')
print(f'O amior número digitado foi {maior_num} e o menor número foi {menor_num}')

valor_total = 0
cont_prod_mil = 0
cont_repeat = 0
menor_preco = 0
guarda_nome = ''

while True:
    cont_repeat += 1

    nome_prod = str(input('Nome do produto: ')).title().strip()
    preco_prod = float(input('Preço R$:'))

    valor_total += preco_prod

    if preco_prod >= 1000:
        cont_prod_mil += 1
    
    if cont_repeat == 1 or preco_prod < menor_preco:
        menor_preco = preco_prod
        guarda_nome = nome_prod
    
    escolha = str(input('Deseja continuar? Responda [S/N]: ')).upper().strip()    
    if escolha != 'S' and escolha != 'N':
        print('Resposta inválida, Tente novamente com respostas sendo apenas "S" para Sim, ou "N" para "Não".')
        continue

    if escolha == 'N':
        break

print(f'Valor total da compra: R${valor_total}')
print(f'Quantidade de produtos a cima de [R$1000.00]: {cont_prod_mil}')
print(f'Poduto mais barato: {guarda_nome}, R${menor_preco}')



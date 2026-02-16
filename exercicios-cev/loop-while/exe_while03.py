primeiro_valor = int(input('Digite primeiro valor: '))
segundo_valor = int(input('Digite segundo valor: '))
decisao = 0

while decisao != 5:
    print('\n---OPERAÇÕES---')
    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior')
    print('[4] novos números')
    print('[5] sair\n')

    decisao = int(input('Deseja fazer qual operação? Responda: '))

    if decisao == 1:
        print(f'A soma entre {primeiro_valor} + {segundo_valor} = {primeiro_valor + segundo_valor}.')
    elif decisao == 2:
        print(f'A multiplicação entre {primeiro_valor} * {segundo_valor} = {primeiro_valor * segundo_valor}.')
    elif decisao == 3:
        if primeiro_valor == segundo_valor:
            print('Os dois números são iguais. Não há maior.')
            continue
        elif primeiro_valor > segundo_valor:
            print(f'Entre {primeiro_valor} e {segundo_valor} o maior é {primeiro_valor}.')
        else:
            print(f'Entre {primeiro_valor} e {segundo_valor} o maior é {segundo_valor}.')
    elif decisao == 4:
        primeiro_valor = int(input('Digite primeiro valor: '))
        segundo_valor = int(input('Digite segundo valor: '))
    elif decisao == 5:
        print('Encerrando...')
    else:
        print('Valor inválido. Tente novamente...')
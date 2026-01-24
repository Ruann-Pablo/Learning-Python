lista_gols = []
lista_jogadores = []
jogador = {}

while True:
    soma_gols = 0
    jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
    quant_partidas = int(input(f'Informe a quantidade de partidas jogadas por {jogador["nome"]}: '))

    for i in range(quant_partidas):
        quant_gols = int(input(f' Informe a quantidade de GOLS feitos por {jogador["nome"]} na {i + 1}ª partida: '))
        lista_gols.append(quant_gols)

    jogador["gols"] = lista_gols[:]

    for i in lista_gols:
        soma_gols += i

    jogador["total_gols"] = soma_gols

    while True:
        resposta = input('Quer continuar? [S/N]: ').lower().strip()
        if resposta in ('s', 'n'):
            break

    lista_jogadores.append(jogador.copy())
    lista_gols.clear()

    if resposta == 'n':
        break

print('-='*30)
for indice, jogador in enumerate(lista_jogadores):
    print(f'{indice} | {jogador["nome"]} | {jogador["gols"]} | {jogador["total_gols"]}')

while True:
    print('-='*30)
    ver_jogador = int(input('Mostrar dados de qual jogador [999 interrompe o programa]: '))
        
    if ver_jogador == 999:
        break
        
    print(f'\nLevantamento do jogador {lista_jogadores[ver_jogador]["nome"]}:')
    
    for indice in range(len(lista_jogadores[ver_jogador]["gols"])):
        print(f'Na {indice + 1}ª partida fez {lista_jogadores[ver_jogador]["gols"][indice]}')

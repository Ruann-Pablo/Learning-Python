lista_gols = []
soma_gols = 0
jogador = {}
jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
quant_partidas = int(input(f'Informe a quantidade de partidas jogadas por {jogador["nome"]}: '))

for i in range(quant_partidas):
    quant_gols = int(input(f' Informe a quantidade de GOLS feitos por {jogador["nome"]} na {i + 1}ª partida: '))
    lista_gols.append(quant_gols)

jogador["gols"] = lista_gols

for i in lista_gols:
    soma_gols += i

jogador["total_gols"] = soma_gols

print('-=' * 30)
print(jogador)

print('-=' * 30)
for c, v in jogador.items():
    print(f'O campo {c} tem  valor: {v}')

print('-=' * 30)
print(f'O jogador {jogador["nome"]}, jogou {quant_partidas} partidas.')

for i, v in enumerate(jogador['gols']):
    print(f'Na partida {i + 1}, fez {jogador["gols"][i]} gols.')
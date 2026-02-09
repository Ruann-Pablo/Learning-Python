retorna_infos_lambda = (
    lambda nome, qnt_gols: f"O jogador {nome}, marcou {qnt_gols} gol(s) no campeonato."
)


def pede_info_jogador(func):
    nome = input("Nome do jogador: ").strip() or "<desconecido>"
    qnt_gols = input("Quantidade de gols: ")

    if not isinstance(qnt_gols, int):
        qnt_gols = 0

    return func(nome, qnt_gols)


print(pede_info_jogador(retorna_infos_lambda))

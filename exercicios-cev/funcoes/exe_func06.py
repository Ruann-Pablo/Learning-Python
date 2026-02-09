from datetime import date


def pede_ano_nascimento(func):
    ano_nascimento = int(input("Informe o ano em que nasceste: "))
    return func(ano_nascimento)


def voto(ano_nascimento):
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento

    if idade in range(18, 75):
        return f"Idade: {idade}\n Voto: Obrigatório"
    elif idade in range(75, 120):
        return f"Idade: {idade}\n Voto: Opcional"
    else:
        return f"Idade: {idade}\nVoto: Não vota"


resp_voto = pede_ano_nascimento(voto)

print(resp_voto)

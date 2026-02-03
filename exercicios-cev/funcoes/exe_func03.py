def mensagem(primeiro_num, segundo_num, passo_num):
    print("-=" * 50)

    if primeiro_num > segundo_num:
        segundo_num += 1
    else:
        segundo_num -= 1

    print(
        f"Contagem de {primeiro_num} até {segundo_num} pulando de {passo_num} em {passo_num}."
    )


def contador(inicio: int, fim: int, passo: int):
    if inicio > fim:
        if passo > 0:
            passo = -passo

        fim -= 1
    else:
        fim += 1

    mensagem(inicio, fim, passo)

    for i in range(inicio, fim, passo):
        print(i, end=" ")
    print("FIM")


def valor_personalizado():
    print("-=" * 50)
    inicio = int(input("Inicio = "))
    fim = int(input("Fim = "))
    passo = int(input("Passo = "))

    contador(inicio, fim, passo)


contador(1, 10, 1)
contador(10, 1, 2)
valor_personalizado()

def maior(*args: int):
    print("Analisando valores...")

    maior_valor = 0
    tamanho = len(args)

    for valor in args:
        print(valor, end=", ")

        if valor > maior_valor:
            maior_valor = valor

    return tamanho, maior_valor


recebe_maior = maior(1, 54, 45, 89, 70)

print(f"Foram informados {recebe_maior[0]} valor(es) ao todo.")
print(f"O maior valor informado foi = {recebe_maior[1]}")

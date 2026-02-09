def leiaInt(texto):
    while True:
        recebe = input(texto)
        if recebe.lstrip("-").isdigit():
            return recebe
        else:
            print("ERRO! Digite um número intero válido.")


n = leiaInt("Digite um número: ")
print(f"Você digitou o número: {n}")

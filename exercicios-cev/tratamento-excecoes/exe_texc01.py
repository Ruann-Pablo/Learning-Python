def leia_int(texto_int):
    while True:
        try:
            recebe_int = int(input(texto_int))
        except (ValueError, TypeError):
            print("Erro: Por favor, digite um número inteiro válido.")
        else:
            return recebe_int


def leia_float(texto_float):
    while True:
        try:
            recebe_float = input(texto_float)

            if not "." in recebe_float:
                raise ValueError
            else:
                float(recebe_float)

        except (ValueError, TypeError):
            print(f"Erro: Por favor, digite um número real válido.")
        else:
            return recebe_float


n_int = leia_int("Digite um número inteiro: ")
n_float = leia_float("Digite um número real: ")

print(f"O valor inteiro digitado foi {n_int}, o valor real foi {n_float}")

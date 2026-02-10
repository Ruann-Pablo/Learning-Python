def leiaDinheiro(texto):
    while True:
        recebe = input(texto).strip().replace(",", ".")
        if recebe.isalpha() or recebe == "":
            print("ERRO! Digite um número intero válido.")
        else:
            return float(recebe)

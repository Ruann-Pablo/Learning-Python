dados = ("user1", "admin22", "guest007")
numeros = tuple(
    int("".join(c for c in i if c.isdigit()))
    for i in dados
    )

print(numeros)
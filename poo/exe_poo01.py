class Produto:
    def __init__(self, nome: str, preco: float) -> None:
        self.nome = nome
        self.preco = preco

    def __str__(self) -> str:
        return f"Produto: {self.nome}, Preço: {self.preco}"


primeiro_produto = Produto("Alicate", 20.50)
segundo_produto = Produto("Martelo", 10.99)

print(primeiro_produto)
print(segundo_produto)

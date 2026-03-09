class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def comer(self):
        print(f"{self.nome} está comendo!")

    def correr(self):
        print(f"{self.nome} está correndo!")


pessoa01 = Pessoa("Ruann", 22)

print(pessoa01.correr)
print(pessoa01.comer)

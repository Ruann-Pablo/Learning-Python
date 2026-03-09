# codigo para testar algo envolvendo herança


class Usuario:
    def __init__(self, nome: str, idade: int) -> None:
        self.__nome = nome
        self.__idade = idade

    def exibir_info_obj(self):
        return self.__dict__

    # metodos para nome
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome

    # metodos para idade
    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade: str) -> None:
        self.__idade = idade


class Aluno(Usuario):
    def __init__(self, nome: str, idade: int, matricula: str) -> None:
        super().__init__(nome, idade)
        self.__matricula = matricula

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula: str):
        self.__matricula = matricula


class Professor(Usuario):
    def __init__(self, nome: str, idade: int, curso: str) -> None:
        super().__init__(nome, idade)
        self.__curso = curso

    @property
    def curso(self):
        return self.__curso

    @curso.setter
    def curso(self, curso: str):
        self.__curso = curso


obj = Professor("Ruann", 22, "POO")
print(obj.exibir_info_obj())

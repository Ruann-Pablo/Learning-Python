from lib.interface import *
from lib.arquivo import *


def menu():
    arq = 'exercicio03.txt'
    if not verifica_arquivo(arq):
        cria_arquivo(arq)
    else:
        while True:
            cabecalho("menu")
            resposta = exibe_opc_menu(
                ["Exibir usuários cadastrados", "Cadastrar usuários", "Sair do programa"]
            )

            if resposta == 3:
                print('Programa encerrado.')
                break


menu()

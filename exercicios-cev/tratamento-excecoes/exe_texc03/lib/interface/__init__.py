from ..usuario_tools import *


def leia_opc(texto):
    while True:
        print('=' * 42)
        res = input(texto)
        try:
            if res.isdigit():
                res_convertida = int(res)

                if not res_convertida in [1, 2, 3]:
                    raise ValueError
                else:
                    if res_convertida == 1:
                        cabecalho('usuários cadastrados')
                        exibir_arquivo()
                    elif res_convertida == 2:
                        cabecalho('novo cadastro')
                        cadastra_usuario()
                    else:
                        return res_convertida
            else:
                raise TypeError

        except ValueError:
            print("ERRO: Por favor, digite uma opção válida.")
        except TypeError:
            print("ERRO: Por favor, digite um número inteiro válido.")


def linha(tamanho=42):
    return "-" * tamanho


def cabecalho(txt):
    print(linha())
    print(txt.center(42).upper())
    print(linha())


def exibe_opc_menu(lista_opcoes):
    for indice, opc in enumerate(lista_opcoes):
        print(f"{indice + 1} - {opc}")
    opcao_resp = leia_opc("Sua opção: ")

    return opcao_resp


def exibir_arquivo():
    with open('/home/ruann/EstudosPython/exercicios-cev/tratamento-excecoes/exe_texc03/exercicio03.txt',
              'r') as arquivo:
        usuarios_exibir = arquivo.readlines()
        for indice, usuario_item in enumerate(usuarios_exibir):
            print(f'{indice} -> {usuario_item.strip("\n")}')

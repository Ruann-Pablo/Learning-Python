def cadastra_usuario():
    while True:
        try:
            usuario = dict()
            usuario['nome'] = str(input('Informe o nome: ')).strip().title()
            usuario['idade'] = int(input('Informe a idade: '))

            if usuario['idade'] < 1 or usuario['idade'] > 120:
                raise ValueError
        except (TypeError, ValueError):
            print('Os dados não foram inseridos incorretamente. Tente novamente.')
        else:
            print(f'Novo registro de {usuario['nome']}  adicionado com sucesso.')
            with open('/home/ruann/EstudosPython/exercicios-cev/tratamento-excecoes/exe_texc03/exercicio03.txt',
                      'a') as arquivo:
                return arquivo.writelines(f'Usuário: {usuario['nome']}, Idade: {usuario['idade']};\n')

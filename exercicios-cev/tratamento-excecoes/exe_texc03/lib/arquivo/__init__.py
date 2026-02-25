def verifica_arquivo(arq_txt):
    try:
        abre_arq = open(arq_txt, 'rt')
        abre_arq.close()
    except FileNotFoundError:
        return False
    else:
        return True


def cria_arquivo(arq_txt):
    while True:
        try:
            cria_aqr = open(arq_txt, 'wt+')
            cria_aqr.close()
            verifica_arquivo(arq_txt)
        except:
            print('Erro ao tentar criar o arquivo. Tente novamente.')
        else:
            return cria_aqr

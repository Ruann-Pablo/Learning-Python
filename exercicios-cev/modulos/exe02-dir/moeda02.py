def aumentar(valor, formatacao=False):
    resultado = valor + (valor * 0.1)

    if formatacao:
        return f'R${resultado:.2f}'.replace('.', ',')

    return resultado


def diminuir(valor, formatacao=False):
    resultado = valor - (valor * 0.1)

    if formatacao:
        return f'R${resultado:.2f}'.replace('.', ',')

    return resultado


def metade(valor, formatacao=False):
    resultado = valor / 2

    if formatacao:
        return f'R${resultado:.2f}'.replace('.', ',')

    return resultado


def dobro(valor, formatacao=False):
    resultado = valor * 2

    if formatacao:
        return f'R${resultado:.2f}'.replace('.', ',')

    return resultado

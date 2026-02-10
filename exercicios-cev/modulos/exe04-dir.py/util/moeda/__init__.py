def aumentar(valor, taxa=10, formatacao=False):
    resultado = valor + (valor * (taxa / 100))

    if formatacao:
        return f"R${resultado:.2f}".replace(".", ",")

    return resultado


def diminuir(valor, taxa=5, formatacao=False):
    resultado = valor - (valor * (taxa / 100))

    if formatacao:
        return f"R${resultado:.2f}".replace(".", ",")

    return resultado


def metade(valor, formatacao=False):
    resultado = valor / 2

    if formatacao:
        return f"R${resultado:.2f}".replace(".", ",")

    return resultado


def dobro(valor, formatacao=False):
    resultado = valor * 2

    if formatacao:
        return f"R${resultado:.2f}".replace(".", ",")

    return resultado


def resumo(preco, aumento, diminuicao):
    print("-=" * 25)
    print(f"Preço analisado: {preco}")
    print(f"O dobro do valor: {dobro(preco, True)}")
    print(f"A metade do valor: {metade(preco, True)}")
    print(f"Aumento de {aumento}%: {aumentar(preco, aumento, True)}")
    print(f"Diminuição de {diminuicao}%: {diminuir(preco, diminuicao, True)}")

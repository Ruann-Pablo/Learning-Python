from random import randint
from typing import List


def sorteia(lista: List[int]):
    print("Sorteando 5 valores: ", end=" ")

    for i in range(0, 5):
        lista.append(randint(0, 10))
        print(lista[i], end=" ")
    print("PRONTO!")

    return lista


def soma(lista_soma: List[int]):
    soma_itens = 0

    for item in lista_soma:
        if item % 2 == 0:
            soma_itens += item

    return lista_soma, soma_itens


lista = []
lista_att = soma(sorteia(lista))


print(f"Somando os valores pares de {lista_att[0]}, temos o valor de: {lista_att[1]}")


# Já que o objeto em "lista = []" foi modificado, poderia ser feito assim:

# ```resultado = soma_pares(numeros)
# print(f"Somando os valores pares de {lista_att}, temos o valor de: {resultado}")```

# A função `soma()` poderia retornar apenas a variável `soma_itens`, tornando o código mais limpo.
# Mas deixa do jeito que tá...

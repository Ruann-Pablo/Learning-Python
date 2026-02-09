def fatorial(func):
    def wrapper(numero, *args, **kwargs):
        if args:
            print(f"{numero}! = ", end="")
            for i in range(numero, 0, -1):
                print(i, end="")
                print(" * " if i > 1 else " = ", end="")

            return func(numero)
        else:
            return func(numero)

    return wrapper


@fatorial
def calcula_fatorial(numero):
    cont = numero
    fatorial = 1

    while cont > 0:
        fatorial *= cont
        cont -= 1

    return fatorial


resultado = calcula_fatorial(5, True)

print(resultado)


# Sei que não havia necessidade da criação de um Decorator além de está mal implementado (eu acho...).
# Mas este exercicio utilizando Decorators, é apenas para fins de estudo e prática pessoal.

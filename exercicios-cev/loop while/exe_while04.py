num = int(input("Digite um número: "))
cont = num
fatorial = 1

print(f"{num}! = ", end="")

while cont > 0:
    print(f"{cont}", end="")
    print(" * " if cont > 1 else " = ", end="")
    fatorial *= cont
    cont -= 1
print(fatorial)

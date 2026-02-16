sexo = ''

while sexo != 'M':
    sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0] # pega aprimeira letra da string.
    # no caso do usuário digitar "masculino", apenas o "m" será capturado e usado na validação.

    if sexo != 'M' and sexo != 'F':
        print('Sexo inválido.')
        continue

print('Registrado com sucesso!')
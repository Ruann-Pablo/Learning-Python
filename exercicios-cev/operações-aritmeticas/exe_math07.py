num = int(input('Digite um número para ver sua tabuada: '))
operacao = str(input('Qual operação deseja da tabuada?\nOperações: \n"*" para Multiplicação\n"/" para Divisão\n"+" para Adição\n"-" para subtração.\n\nEscolha: '))

if (operacao == '*'):
    for i in range(11):
        print(f'{num} * {i} = {num * i}')

if (operacao == '/'):
    for i in range(11):
        print(f'{num} / {i} = {num / i}')

if (operacao == '+'):
    for i in range(11):
        print(f'{num} + {i} = {num + i}')

if (operacao == '-'):
    for i in range(11):
        print(f'{num + i} - {i} = {(num + i) - num}')
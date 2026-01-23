trabalhador = {}

while True:
    trabalhador['nome'] = str(input('Nome: ')).strip().title()
    ano_nascimento = int(input('Ano de nascimento: '))
    
    if ano_nascimento > 2018:
        print('Ano inválido. Tente novamente')
    else:
        trabalhador['idade'] =  2018 - ano_nascimento
        if trabalhador['idade'] < 14:
            print('Idade inválida para trabalho.')
            break

        trabalhador['ctps'] = int(input('Carteira de trabalho (0 se não tem): ')) 
        if trabalhador['ctps'] == 0:
            break

        trabalhador['ano_contratacao'] = int(input('Ano de contratação: '))
        trabalhador['salario'] = float(input('Salário: '))
        trabalhador['aposentadoria'] = trabalhador['idade'] + ((trabalhador['ano_contratacao'] + 35) - 2018)

        break

print('-' * 30)
for c, v in trabalhador.items():
    print(f'{c} tem valor {v}')
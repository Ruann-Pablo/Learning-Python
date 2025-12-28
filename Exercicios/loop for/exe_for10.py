cont_mulher = 0
mais_velho = ''
soma_idade = 0
guarda_idade = 0
media_idade = 0
divisor_media = 0

for i in range(1, 5):
    nome = str(input('\nNome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()

    if idade <= 0:
        print('Idade inválida')
        continue

    if sexo != 'M' and sexo != 'F':
        print('Sexo inválido.')
        continue

    if sexo == 'F' and idade < 20:
        cont_mulher += 1

    if sexo == 'M' and guarda_idade < idade:
        mais_velho = nome
        guarda_idade = idade
    
    divisor_media += 1
    soma_idade += idade

media_idade = soma_idade / divisor_media

print(f'A média de idade do grupo é de {media_idade:.1} anos.')
if mais_velho:
    print(f'O homem mais velho tem {guarda_idade} anos se chama {mais_velho}')
else:
    print('Não há homens no grupo.')

print(f'Ao todo são {cont_mulher} mulheres com menos de 20 anos')

from datetime import date

ano_atual = date.today().year
cont_maior = 0
cont_menor = 0

# print(ano_atual)

for i in range(1, 8):
    ano_nasc = int(input(f'Informe o ano em que a {i}ª pessoa nasceu: '))

    if ano_nasc <= 1900:
        print('Haja disposição para viver tanto! hahaha!')
        continue
    
    if ano_nasc > ano_atual:
        print('Nem saiu do saco do pai e já quer fazer graça?!')
        continue

    if ano_atual - ano_nasc < 18:
        cont_menor += 1
    else:
        cont_maior += 1

print(f'Ao todo tivemos {cont_maior} pessoas maiores de idade.')
print(f'Ao todo tivemos {cont_menor} pessoas menores de idade.')
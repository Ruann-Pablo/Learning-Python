# preco = float(input('Qual o valor do produto? R$: '))
# desconto = preco * 0.05

# print(f'{preco - desconto}')

preco = float(input('Qual o valor do produto? R$: '))
porcentagem = 0.05
desconto = preco - (preco * porcentagem)

print(f'O produto que custava R${preco}, na promoção vai custar R${desconto:.2f}')


val_dia = 60.00
val_km = 0.15

qnt_dias = int(input('Quantos dias alugados? Responda: '))
kms_rdd = float(input('Quantos Km rodados? Responda: '))

valor_total = (qnt_dias * val_dia) + (kms_rdd * val_km)

print(f'O valor total a pagar é de: R${valor_total:.2f}')
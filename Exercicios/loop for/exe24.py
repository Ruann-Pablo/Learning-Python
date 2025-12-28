primo = int((input('Digite um número: ')))
contador = 0


for i in range(1, primo + 1):
    if primo % i == 0:
        contador += 1

if contador == 2:
    print(f'{primo} é um número primo!')
else:
    print(f'{primo} não é um número primo')
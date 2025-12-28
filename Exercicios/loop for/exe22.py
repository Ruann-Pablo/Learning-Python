termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + (10 - 1) * razao

for i in range (termo, decimo + razao, razao):
    print(i, end='-> ')

print('PA')
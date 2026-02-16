termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
i = 1

while i <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    i += 1
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
mais = 10
j = 0
i = 1

while mais != 0:
    j += mais
    while i <= j:
        print(f'{termo} -> ', end='')
        termo += razao
        i += 1
    mais = int(input('\nQuantos termos você quer ver a mais? Responda: '))
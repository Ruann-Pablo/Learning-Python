tupla = ('Abelha', 'Urso', 'Arara', 'Macaco')

for i in tupla:
    print(f'\nNa palavra {i} temos as vogais: ', end='')
    for c in i: 
        if c.lower() in 'aeiou':
            print(c.lower(), end=' ')



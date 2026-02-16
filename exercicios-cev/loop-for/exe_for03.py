soma = 0

for i in range(0, 501): # ```range(1, 501, 2)``` isso faz com que ja obetenhamos os impares sem precisarmos...
    if i % 2 == 1: # <- dessa dupla verificação.
        if i % 3 == 0: # usando apenas esta condição.
            soma += i

print(f'A soma de todos os números impares múltiplos de 3, é de: {soma}')
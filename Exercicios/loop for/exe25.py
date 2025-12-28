palindromo = str(input('Digite uma palvara ou frase: ')).strip().lower()
separado = palindromo.split()
junto = ''.join(separado)
inverso = ''

for i in range(len(junto) - 1, -1, -1):
    inverso += junto[i]

print(f'\nPalavra: "{junto}"')
print(f'Palavra invertida: "{inverso}"')

if inverso == junto:
    print('É um palindromo!')
else:
    print('Não é um palindromo!\n')
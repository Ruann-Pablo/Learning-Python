nome = str(input('Digite seu nome completo: ')).title().strip()

print('Analisando seu nome...')
print(f'Seu nome maiusculo: {nome.upper()}')
print(f'Seu nome minusculo: {nome.lower()}')
# O count() vai contar quantas vezes aparece determinado caractere na string.
# Neste caso ele está contando quantos espaços vazios exitem na string e subtraindo na contagem do tamanho feito pelo método len().
print(f'Seu nome tem o tamanho total de caracteres de: {len(nome) - nome.count(" ")}')

# Dividir a string com split() talvez não seja uma boa opção para acessar APENAS, o primeiro nome da string.
nome_separado = nome.split(" ")
print(f'Seu primeiro nome "{nome_separado[0]}" tem o tamanho total de caracteres de: {len(nome_separado[0])}')

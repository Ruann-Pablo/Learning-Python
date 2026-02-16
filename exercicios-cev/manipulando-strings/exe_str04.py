frase = str(input('Digite uma frase: ')).strip().lower()

print(f'A letra "a" aparece {frase.count('a')} na frase digitada.')
print(f'A primeira letra "a" aparece na posicao {frase.find('a')+1}.')
print(f'A ultima letra "a" aparece na posicao {frase.rfind('a')+1}.')
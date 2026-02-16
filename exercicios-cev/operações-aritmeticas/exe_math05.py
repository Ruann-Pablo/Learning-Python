# Exercício: Desenvolva um programa que leia as notas de um anluno e eiba a média.

quant_notas = 0
soma_nota = 0

while True:
    nota = float(input('Informe a nota do aluno: '))
    soma_nota += nota
    quant_notas += 1

    resposta = int(input('Deseja adicionar mais uma nota? [s/n] ')).lower()

    if resposta == 'n':
        break

media = soma_nota / quant_notas

print(f'Media do aluno: {media:.1f}')
print('cadastre uma pessoa'.upper())
print('-'*25)

quant_maioridade = 0
quant_homem = 0
quant_mulher = 0

while True:
    idade = int(input('Idade: '))

    if idade < 0:
        print('Idade inválida. Tente novamente.')
        continue

    if idade > 18:
        quant_maioridade += 1

    sexo = str(input('Sexo [M/F]: ')).upper().strip()

    if sexo != 'M' and sexo != 'F':
        print('Sexo inválido. Tente novamente.')
        continue

    if sexo == 'F' and idade < 20:
        quant_mulher += 1
    elif sexo == 'M':
        quant_homem += 1

    escolha = str(input('Deseja continuar? Responda [S/N]: ')).upper().strip()
    
    if escolha != 'S' and escolha != 'N':
        print('Resposta inválida, Tente novamente com respostas sendo apenas "S" para Sim, ou "N" para "Não".')
        continue

    if escolha == 'N':
        break

    print('-'*25)

print(f'Total de pessoas com mais de 18 anos: {quant_maioridade}')
print(f'Total de homens cadastrados: {quant_homem}')
print(f'Total de mulheres cadastradas com menos de 20 anos: {quant_mulher}')

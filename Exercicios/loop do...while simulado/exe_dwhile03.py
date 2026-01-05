from random import randint

vitoria = 0

while True:
    print('Vamos jogar PAR ou ÍMPAR')
    print('-'*20)

    valor_computador = randint(0, 10)
    valor = int(input('Digite um valor (de 0 à 10): '))

    if valor < 0 and valor > 10:
        print('Valor inválido. Tente novamente.')
        continue

    escolha = str(input('Par ou Ímpar [P/I]: ')).upper().strip()

    soma_valores = valor + valor_computador
    
    if escolha == 'P':
        if soma_valores % 2 == 0:
            print(f'Você jogou {valor} e o computador {valor_computador}. Total de {soma_valores} DEU PAR')
            print('Você venceu!')
            vitoria += 1
        else:
            print(f'Você jogou {valor} e o computador {valor_computador}. Total de {soma_valores} DEU ÍMPAR')
            print('Você perdeu!')
            break
    elif escolha == 'I':
        if soma_valores % 2 == 1:
            print(f'Você jogou {valor} e o computador {valor_computador}. Total de {soma_valores} DEU ÍMPAR')
            print('Você venceu!')
            vitoria += 1 
        else:
            print(f'Você jogou {valor} e o computador {valor_computador}. Total de {soma_valores} DEU PAR')
            print('Você perdeu!')
            break
    else:
        print('Escolha inválida. Selecione "P" para Par, ou "I" para Ímpar.')
        continue

print(f'Você venceu a máquina em {vitoria} partidas!' if vitoria > 0 else 'Você não venceu a máquina desta vez...')
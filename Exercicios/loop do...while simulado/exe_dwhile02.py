while True:
    print('='*46)
    numero = int(input('Digite o número que desejas ver a tabuada: '))
    
    if numero <= 0:
        print('Não é possível fazer o calculo deste valor. Tente nvamente.')
        continue

    for i in range(1, 11):
        print(f'{numero} x {i} = {numero * i}')

    resposta = str(input('Deseja continuar [s/n]? Responda: ')).lower().strip()

    if resposta != 's' and resposta != 'n':
        print('Resposta inválida, Tente novamente com respostas sendo apenas "s" para Sim, ou "n" para "Não".')
        continue
    

    if resposta == 'n':
        print('Programa tabuada encerrado.')
        break
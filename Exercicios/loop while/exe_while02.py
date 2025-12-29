import random

num_aleatorio = random.randint(1, 50)
guarda_resposta = 0
cont_tentativas = 0

print('Pensei em um número aleatório entre 1 e 10.')
print('Será que você consegue adivinhar?\n')

while num_aleatorio != guarda_resposta:
    guarda_resposta = int(input('Qual o seu palpite? Responda: '))

    cont_tentativas += 1

    if guarda_resposta > num_aleatorio:
        print('Menos... Tente novamente.\n')

    if guarda_resposta < num_aleatorio:
        print('Mais... Tente novamente.\n')

print(f'Parabéns! Você acertou com {cont_tentativas} tentativas!')
    
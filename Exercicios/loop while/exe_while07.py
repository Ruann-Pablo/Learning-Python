n = int(input('Quantos termos você quer mostrar? Responda: '))
anterior_termo = 0
atual_termo = 1
prox_termo = 0
i = 3

print('0 -> 1', end=' -> ')

while i <= n:
    prox_termo = atual_termo + anterior_termo
    anterior_termo = atual_termo
    atual_termo = prox_termo

    print(atual_termo, end=' -> ')
    i += 1

print('Fim')
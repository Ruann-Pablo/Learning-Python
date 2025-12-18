salario_atual = float(input('Qual o salário atual do funcionário? R$: '))
ajuste = 0.15
novo_salario = salario_atual + (salario_atual * ajuste)

print(f'Um funcionário que recebia R${salario_atual}, com 15% de aumento, passa receber: R${novo_salario:.2f}')
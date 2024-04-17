"""Faça um algoritmo que receba o salário-base de um funcionário. Calcule e mostre o
salário a receber, sabendo-se que esse funcionário tem gratificação de 5% sobre o
salário-base e paga imposto de 7% sobre o salário-base."""

salario_base = float(input('Digite o salario-base: '))
gra = float(input('Digite o valor da gratificaçao: '))
desconto = float(input('Digite o valor do imposto: '))

salario_imposto = ((salario_base * (gra / 100)) + salario_base) - (salario_base * (desconto / 100))

print("seu salario é: ", salario_imposto)
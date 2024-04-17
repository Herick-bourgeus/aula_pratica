"""Faça um algoritmo que receba o salário-base de um funcionário. Calcule e mostre o seu
salário a receber, sabendo-se que esse funcionário tem gratificação de R$500,00 e paga
imposto de 10% sobre o salário-base."""


salario_base = float(input('Digite o salario-base: '))
#gra = float(input('Digite o valor da gratificaçao: '))
gra = 500
desconto = float(input('Digite o valor do imposto: '))

salario_imposto = (gra + salario_base) - (salario_base * (desconto / 100))

print("seu salario é: ", salario_imposto)
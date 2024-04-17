"""Faça um algoritmo que receba o salário de um funcionário e o percentual de aumento.
Calcule e mostre o valor do aumento e o novo salário."""


salario = float(input("digite o seu salario: "))
porcentagem = float(input("digite a porcentage: "))

aumento = (salario * (porcentagem / 100)) + salario
valor_aumento = salario * (porcentagem / 100)

print("seu salario atual: ", aumento)
print("o valor de amento: ", valor_aumento)
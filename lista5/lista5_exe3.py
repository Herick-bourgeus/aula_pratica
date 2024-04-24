"""Dado o salário de um indivíduo, calcule o imposto de renda a ser pago com base nas
seguintes faixas:
● Salários até R$ 1903,98: isento
● Salários de R$ 1903,99 até R$ 2826,65: 7.5%
● Salários de R$ 2826,66 até R$ 3751,05: 15%
● Salários acima de R$ 3751,05: 22.5%
"""

salario = float(input("Digite o seu salario:"))

if salario <= 1903.98:
    print("Seu salario não está insento de imposto")
elif salario >= 1903.99 and salario <= 2826.65:
    salario_imposto = salario * 0.075
    salario_novo = salario - salario_imposto
    print("voce ira pagar um mposto de R${:.2f}".format(salario_novo))
    print("se novo salario é de R${:.2f}".format(salario_imposto))
elif salario >= 2826.66 and salario <= 3751.05:
    salario_imposto = salario * 0.15
    salario_novo = salario - salario_imposto
    print("voce ira pagar um mposto de R${:.2f}".format(salario_novo))
    print("se novo salario é de R${:.2f}".format(salario_imposto))
elif salario >= 3751.05:
    salario_imposto = salario * 0.225
    salario_novo = salario - salario_imposto
    print("voce ira pagar um mposto de R${:.2f}".format(salario_novo))
    print("se novo salario é de R${:.2f}".format(salario_imposto))
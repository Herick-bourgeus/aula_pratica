"""Um funcionário recebe um salário fixo mais 4% de comissão sobre as vendas. Faça um
programa que receba o salário fixo do funcionário e o valor de suas vendas, calcule e
mostre a comissão e o salário final do funcionário."""

salario_fixo = float(input("Digite o salário fixo do funcionário: "))
vendas = float(input("Digite o valor das vendas do funcionário: "))

comissao = vendas * 0.04
salario_final = salario_fixo + comissao

print(f"A comissão do funcionário é: R$", comissao)
print(f"O salário final do funcionário é: R$", salario_final)

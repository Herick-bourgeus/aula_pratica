"""Faça um programa que receba o custo de um espetáculo teatral e o preço do convite
desse espetáculo. Esse programa deve calcular e mostrar a quantidade de convites que
devem ser vendidos para que pelo menos o custo do espetáculo seja alcançado."""

custo_espetaculo = float(input("Digite o custo do espetáculo teatral: "))
preco_convite = float(input("Digite o preço do convite: "))

quantidade_convites = custo_espetaculo / preco_convite + 1

print(f"Para cobrir o custo do espetáculo, devem ser vendidos pelo menos {quantidade_convites} convites.")

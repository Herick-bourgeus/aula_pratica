"""Faça um programa que receba o preço de um produto. Calcule e mostre o novo preço,
sabendo-se que este sofreu um desconto de 10%."""

preco = float(input("Digite o preço do produto: "))

novo_preco = preco * 0.9

print(f"O novo preço do produto, com desconto de 10%, é: R${novo_preco:.2f}")
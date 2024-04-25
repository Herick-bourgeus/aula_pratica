""" O cardápio de uma casa de lanches é dado pela tabela abaixo:

Escreva um programa que leia o código do item adquirido pelo consumidor e a quantidade,
calculando e mostrando o valor a pagar. Não será necessário exibir o produto e o valor,
somente o valor final.
"""

codigo = int(input("Digite o codigo do produto: "))
qtd = int(input("Digite a quantidade de unidades: "))

if codigo == 100:
    valor_final = qtd * 1.70
    print(f"o valor de {qtd} cachorro quente foi de R${valor_final:.2f}")
elif codigo == 101:
    valor_final = qtd * 2.30
    print(f"o valor de {qtd} bauru simples foi de R${valor_final:.2f}")
elif codigo == 102:
    valor_final = qtd * 2.60
    print(f"o valor de {qtd} bauru com ovo foi de R${valor_final:.2f}")
elif codigo == 103:
    valor_final = qtd * 2.40
    print(f"o valor de {qtd} hamburguer foi de R${valor_final:.2f}")
elif codigo == 104:
    valor_final = qtd * 2.50
    print(f"o valor de {qtd} cheeseburguer foi de R${valor_final:.2f}")
elif codigo == 105:
    valor_final = qtd * 1
    print(f"o valor de {qtd} refrigerante foi de R${valor_final:.2f}")


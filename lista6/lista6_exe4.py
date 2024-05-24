"""Faça um algoritmo para imprimir os múltiplos de 5 em um intervalo informado pelo usuário.
"""

print("digite o intervalo para os multiplo de 5")
intervalo1 = int(input("digite o primeiro numero: "))
intervalo2 = int(input("digite o segundo numero: "))
multiplo = 5

for i in range(intervalo1, intervalo2 + 1):
    if i % 5 == 0:
        print(i)
"""Faça um algoritmo para imprimir a soma dos números entre um intervalo determinado pelo
usuário, incluindo os limites inferiores e superiores.
"""

n1 = int(input("digie o primeiro valor: "))
n2 = int(input("digite o segundo valor: "))
soma = 0
for i in range(n1, n2 + 1):
    soma = soma + i

print(f"o valor da soma é: {soma}")
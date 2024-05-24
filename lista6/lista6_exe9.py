"""Faça um algoritmo para calcular o cubo e o quadrado de todos os números pertencentes a um
intervalo, incluindo o limite superior e inferior. """

num1 = int(input("digite o primeiro numero: "))
num2 = int(input("digite o ultimo numero: "))
cubo = 0
quadrado = 0

for i in range(num1, num2+1):
    cubo = i ** 3
    quadrado = i ** 2
    print(f"o valor de {i} elevado ao cubo é {cubo}")
    print(f"o valor de {i} elevado ao quadrado é {quadrado}")
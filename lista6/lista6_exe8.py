""" Faça um algoritmo para ler cinco números e imprimir o cubo e o quadrado de cada um deles. """

num = {int(input("digite o primeiro numero: ")), int(input("digite o segundo numero: ")), int(input("digite o teceiro numero: ")),
       int(input("digite o quarto numero: ")), int(input("digite o quinto numero: "))}
cubo = 0
quadrado = 0

for n in num:
    cubo = n ** 3
    quadrado = n ** 2
    print(f"o valor de {n} elevado ao cubo é de {cubo}")
    print(f"o valor de {n} elevado ao quadrad é de {quadrado}")
    
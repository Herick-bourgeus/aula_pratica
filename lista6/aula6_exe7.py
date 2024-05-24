"""Elabore um algoritmo para calcular a soma dos números ímpares de 1000 a 10. """

soma = 0
for i in range(1001, 9, -2):
  soma += i
print("A soma dos números ímpares de 1000 a 10 é:", soma)

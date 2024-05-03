numeros = [45, 32, 89, 11, 73]
minimo = numeros[0]
maximo = numeros[0]
for numero in numeros:
    if numero < minimo:
        minimo = numero
    if numero > maximo:
        maximo = numero
print("o menor número é: ", minimo)
print("o maior número é: ", maximo)
""" Faça um algoritmo que imprima todos os números de 1 até um número especificado pelo
usuário e a soma deles. """

num = int(input("digite um numero: "))
soma = 0
for i in range(1,num + 1):
    soma += i
    print(i)

print("a soma desses valores é: ", soma)
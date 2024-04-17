"""faça um programa que indentifique entre dois numeros o menor"""

num1 = int(input('digite o primeiro numero: '))
num2 = int(input('digite o segundo o numero: '))

if num1 > num2:
    print("o menor numero: ", num2)
    print("o maior numero: ", num1)
elif num2 > num1:
    print("o menor numero:",num1)
    print("o maior numero:",num2)
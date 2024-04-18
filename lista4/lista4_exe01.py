""" Escreva um programa que pergunte a idade do usuário. Se ele tiver menos de 18 anos
ou mais de 65 anos, informe que ele tem direito a meia-entrada. Caso contrário, informe que
ele deve pagar a entrada inteira.
"""

idade = int(input("Digite a sua idade: "))

if idade <= 18 or idade >= 65:
    print("você tem direito a meia etrada!")

else:
    print("você tem que pagar a entrada inteira!")
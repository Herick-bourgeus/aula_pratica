"""Faça um programa que receba duas notas, calcule e mostre a média ponderada dessas
notas, considerando peso 2 para a primeira nota e peso 3 para a segunda nota.
"""

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media_ponderada = (nota1 * 2 + nota2 * 3) / (2 + 3)

print(f"A média ponderada das notas é: {media_ponderada:.2f}")

"""Crie um programa que pergunte ao usuário se o evento que ele vai é formal ou informal.
Se for formal, recomende o uso de traje social. Se for informal, recomende jeans e
camiseta.
"""

tipo_evento = input("O evento que você vai é formal ou informal? ")

if tipo_evento == "formal":
    print("Use traje social.")
elif tipo_evento == "informal":
    print("Use jeans e camiseta.")
else:
    print("Por favor, responda apenas 'formal' ou 'informal'.")

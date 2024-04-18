"""Faça um programa que pergunte ao usuário a temperatura atual da sala e a temperatura
desejada. Se a temperatura atual estiver abaixo da desejada, informe que o aquecedor será
ligado. Se estiver acima, informe que o ar-condicionado será ligado.
"""

temperatura_atual = float(input("Qual é a temperatura atual da sala? "))
temperatura_desejada = float(input("Qual é a temperatura desejada? "))

if temperatura_atual < temperatura_desejada:
    print("O aquecedor será ligado.")
elif temperatura_atual > temperatura_desejada:
    print("O ar-condicionado será ligado.")
else:
    print("A temperatura atual já está de acordo com a desejada.")

""" Escreva um programa que pergunte ao usuário o estado de destino de um pacote e o
peso do pacote. Se o pacote for para o mesmo estado e pesar menos de 5 kg, informe que
o frete é gratuito. Caso contrário, calcule o frete baseado no peso (R$10,00 por kg). Se o
destino for outro estado, calcule um adicional de R$20,00.
"""

estado_destino = input("Qual é o estado de destino do pacote (mesmo/outro)? ")
peso = float(input("Qual é o peso do pacote em kg? "))

custo_por_kg = 10
custo_adicional_estado = 20

if estado_destino == "mesmo":
    if peso < 5:
        print("O frete é gratuito!")
    else:
        custo_total = peso * custo_por_kg
        print(f"O frete custará R$",custo_total)
elif estado_destino == "outro":
    custo_total = peso * custo_por_kg + custo_adicional_estado
    print(f"O frete custará R$,",custo_total)
else:
    print("opção invalida")
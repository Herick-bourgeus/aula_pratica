"""Escreva um programa que peça ao usuário a classificação etária de um filme (por
exemplo, livre, 12, 16, 18). Peça a idade do usuário e diga se ele pode ou não assistir ao
filme.
"""

print("classifique o filme.")
print("L se for livre para todas as idades.")
print("12 se for acima de 12 anos.")
print("16 se for acima de 16 anos.")
print("18 se for acima de 18 anos.")

classificacao = input("qual a clasificação do filme que deseja ver: ")
idade = int(input("qual a sua idade: "))

if classificacao == "l" or "L":
    print("você pode assistir ao filme! ")

elif classificacao == "12" and idade >= 12:
    print("você pode assistir ao filme! ")

elif classificacao == "16" and idade >= 16:
    print("você pode assistir ao filme! ")

elif classificacao == "18" and idade >= 18:
    print("você pode assistir ao filme! ")

else:
    print("você não pode assistir ao filme! ")
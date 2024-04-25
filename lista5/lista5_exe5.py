"""Criar um programa para identificar se um dia da semana (numerados de 1 a 7) é dia de
semana, fim de semana ou um dia inválido;
"""

dia = int(input("Digite um número de 1 a 7 para identificar o dia da semana:"))

if dia >= 1 and dia <= 5:
    print("Dia útil")
elif dia == 6 or dia == 7:
    print("Fim de semana")
else:
    print("Dia inválido")
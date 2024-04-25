"""Criar um programa para identificar se um mês digitado pelo usuário é de alta ou baixa
temporada (considerar os seguintes meses como alta temporada: dezembro a fevereiro,
junho e julho).
"""

numero_mes = int(input("Digite o número do mês (1-12): "))

alta_temporada = [12, 1, 2, 6, 7]  

if numero_mes in alta_temporada:
    print("Este é um mês de alta temporada.")
else:
    print("Este é um mês de baixa temporada.")
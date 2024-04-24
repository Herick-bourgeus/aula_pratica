"""Escreva um programa onde o usuário insere a velocidade de um carro. Se a velocidade
for superior a 80 km/h, calcule e exiba a multa, cobrando R$ 5,00 por cada km acima do
limite."""

velocidade = float(input("Digite a velocidade do carro: "))

if velocidade_carro > 80:
    # Calcula a multa
    multa = (velocidade_carro - 80) * 5
    print(f"Você ultrapassou o limite de velocidade em {velocidade_carro - 80} km/h.")
    print(f"Sua multa é de R$ {multa:.2f}.")
else:
    print("Você está dentro do limite de velocidade. Dirija com segurança!")

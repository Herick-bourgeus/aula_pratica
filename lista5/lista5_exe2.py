""" Crie um programa que aplique descontos progressivos em uma compra. Solicite o valor
da compra e aplique 10% de desconto se o valor for menor que R$100, 15% de desconto se
for entre R$100 e R$500, e 20% se for maior que R$500"""

valor_produtos = float(input('Digite o valor do produto: '))

if valor_produtos < 100:
    valor_final = valor_produtos * 0.90
    print("você obteve um desconto de 10%")
    print(f" valor do produto é de R${valor_final:.2f}")
elif 100 < valor_produtos < 500:
    valor_final = valor_produtos * 0.85
    print("você obteve um desconto de 15%")
    print(f" valor do produto é de R${valor_final:.2f}")
else:
    valor_final = valor_produtos * 0.80
    print("você obteve um desconto de 20%")
    print(f" valor do produto é de R${valor_final:.2f}")

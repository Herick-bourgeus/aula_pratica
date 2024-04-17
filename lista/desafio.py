"""Desenvolva um programa em Python que calcule o
valor final de uma compra após aplicar um desconto.
O programa deve solicitar ao usuário o valor original
da compra e o percentual de desconto. O desconto
deve ser aplicado sobre o valor original, e o programa
deve exibir tanto o valor do desconto quanto o valor
final da compra após o desconto"""

#entrada de dadoos
valor_compra = float(input('Digite o valor da compra: '))
percentual_desconto = float(input('Digite o percentual do desconto: '))

#calculo desconto e valor
valor_final = valor_compra - (valor_compra * (percentual_desconto / 100))
valor_desconto = valor_compra * (percentual_desconto / 100)

#saida de dados
print('O valor do final é R$', valor_final)
print("o desconto foi de R$", valor_desconto)
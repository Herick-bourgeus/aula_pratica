"""
Sabe-se que o quilowatt de energia custa um quinto do salário mínimo. Faça um
programa que receba o valor do salário mínimo e quantidade de quilowatts consumida
por uma residência. Calcule e mostre:
a) O valor, em reais, de cada quilowatt;
b) O valor, em reais, a ser pago por essa residência;
c) O valor, em reais, a ser pago com desconto de 15%."""

salario_minimo = float(input("Digite o valor do salário mínimo: "))
quilowatt = salario_minimo / 5

print(f"O valor de cada quilowatt é R$", quilowatt)

quilowatts_consumidos = float(input("Digite a quantidade de quilowatts consumida: "))
valor_a_pagar = quilowatts_consumidos * quilowatt

print(f"O valor a ser pago pela residência é R$", valor_a_pagar)

valor_com_desconto = valor_a_pagar * 0.85
print(f"O valor a ser pago com desconto de 15% é R${valor_com_desconto:.2f}")
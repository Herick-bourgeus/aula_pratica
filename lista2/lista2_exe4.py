"""O custo ao consumidor de um carro novo é a soma do preço de fábrica com o
percentual de lucro do distribuidor e dos impostos aplicados ao preço de fábrica. Faça
um programa que recebo o preço de fábrica de um veículo, o percentual de lucro do
distribuidor e o percentual de impostos. Calcule e mostre:
a) O valor correspondente ao lucro do distribuidor;
b) O valor correspondente aos impostos;
c) O preço final do veículo.
"""

fabricante = float(input("Digite o preço  de fabrica: "))
lucro = float(input("Digite o percentual de lucro distribuidor: "))
imposto = float(input("Digite o percentual de imposto: "))

lucro2 =fabricante * (lucro / 100)
imposto2 = fabricante * (imposto / 100)
valor_final = fabricante + lucro2 + imposto2

print("lucro do distribuidor", lucro2)
print("valor do imposto", imposto2)
print("o valor final sera de R$", valor_final)
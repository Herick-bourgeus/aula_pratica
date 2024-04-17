"""Faça um programa que receba o valor de um depósito e o valor da taxa de juros. Calcule
e mostre o valor do rendimento e o valor total depois do rendimento."""

val = float(input('Digite o valor do deposito: '))
rend = float(input('digite a taxa de juros anual: '))
meses = int(input('Digite a quantidade de meses: '))

rendimeto = (val * (((rend/100) / 12) * meses )) + val

print('O valor da rendimento é: ', rendimeto)
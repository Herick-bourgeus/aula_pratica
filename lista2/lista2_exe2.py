"""Faça um programa que receba dois números inteiros. Calcule e mostre um elevado ao
outro."""

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '
               ''))

elevado = n1 ** n2

print("{} elevado a {} é {} ".format(n1, n2, elevado))
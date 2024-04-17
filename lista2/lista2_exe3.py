"""Faça um programa que receba o ano de nascimento de uma pessoa e o ano atual.
Calcule e mostre:
a) A idade dessa pessoa;
b) Quantos anos essa pessoa terá em 2035."""

ano_nascimento = int(input('Digite o ano de nascimento: '))
ano_atual = int(input('Digite o ano atual: '))

idade = ano_atual - ano_nascimento
ano_2035 = 2035 - ano_nascimento

print("voce tem {} anos".format(idade))
print("você tera {} anos de idade em 2035".format(ano_2035))
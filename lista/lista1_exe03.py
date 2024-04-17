"""Faça um algoritmo que receba três notas e seus respectivos pesos. Calcule e mostre a
média ponderada dessas notas."""


#notas
nota1 = float(input('digite a primeira nota do aluno: '))
nota2 = float(input('digite a segunda nota do aluno: '))
nota3 = float(input('digite a terceira nota do aluno: '))

#peso das notas
peso1 = float(input('digite o peso da primeira nota:'))
peso2 = float(input('digite o peso da segunda nota: '))
peso3 = float(input('digite o peso da terceira nota'))

#calculo
media = ((nota1 * peso1) + (nota2 * peso2) + (nota3 + peso3))  / (peso1 + peso2 + peso3)


print('a media é: ', media)
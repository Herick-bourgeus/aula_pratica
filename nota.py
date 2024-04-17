"""Faça um programa para calcular a media poderada de um aluno"""

#notas
nota1 = float(input('digite a primeira nota do aluno: '))
nota2 = float(input('digite a segunda nota do aluno: '))

#peso das notas
peso1 = float(input('digite o peso da primeira nota:'))
peso2 = float(input('digite o peso da segunda nota: '))

#calculo
media = ((nota1 * peso1) + (nota2 * peso2)) / (peso1 + peso2)


print('a media é: ', media)
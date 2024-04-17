"""Faça um programa que receba quatro nota de um aluno, calcule e mostre a madeia aritimetica das
notase a mensagem de aprovaça e reprovção, considerando a aprvaçao media 7 """

n1 = float(input('nota 1: '))
n2 = float(input('nota 2: '))
n3 = float(input('nota 3: '))
n4 = float(input('nota 4: '))

media = (n1 + n2 + n3 + n4) / 4

print("sua média foi: ", media)

if media > 7:
    print('Aprovado')
else:
    print('Reprovado')
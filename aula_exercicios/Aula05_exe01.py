"""refaça o exercicio da media ponderada, mostrando ao usuario
se o aluno foi aprovado ou reporvado,
usando a seguinte regra
media >= 6: aprovado
media <6: reprovado"""

nota1 = float(input('digite a primeira nota do aluno: '))
nota2 = float(input('digite a segunda nota do aluno: '))

#peso das notas
peso1 = float(input('digite o peso da primeira nota:'))
peso2 = float(input('digite o peso da segunda nota: '))

#calculo
media = ((nota1 * peso1) + (nota2 * peso2)) / (peso1 + peso2)

if media >= 6:
    print('aluno aprovado')
else:
    print('aluno reprovado')

print('a media é:', media)
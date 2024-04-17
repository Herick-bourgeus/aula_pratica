"""faça um progrma que receba duas notas e calcule e mostre a media aritmetica e mostre  """

nota1 = float(input('digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))

media = (nota1 + nota1) / 2

print('sua nota é: ', media)

if media >= 7:
    print('Aprovado')
elif media == 4:
    print('exame')
else:
    print('reprovado')

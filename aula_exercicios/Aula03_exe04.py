"""faça um programa que solicite ao ususario quatro numeros.
O programa deve calcular a media aritmetica desses numeros e exibir
oresultado. a media é calculada somandotodos os numeros. por exemplo, se os numeros forem 5, 10,15 e 20,
a media é 12.5"""

a = float(input('Digite o primeiro numero: '))
b = float(input('digite o segundo numero: '))
c = float(input('digite o terceiro numero: '))
d = float(input('digite o quarto numero: '))

media = (a + b + c + d) / 4

"""soma = a + b + c + d / 4
 media = soma / 4"""

print('A media é:', media)



salario = float(input('Digite o valor do seu salario para o reajuste: '))

salario_baixo = salario + (salario * 0.35)
salario_alto = salario + (salario * 0.15)

if salario <= 3000:
    print('O seu salario foi reajustado para R$ ', salario_baixo)
else:
    print('O seu salario foi reajustado para R$', salario_alto)
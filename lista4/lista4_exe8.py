""" Faça um programa que pergunte ao usuário se ele prefere suco ou refrigerante. Se
escolher suco, pergunte se prefere laranja ou uva. Informe o preço da bebida escolhida.
Para sucos o valor é de R$18,90. Para refrigerantes, o valor é de R$6,00."""


print("escolha sua bebida.")
print("se deseja refrigerante digite 1.")
print("se deseja suco digite 2.")
bebida = int(input('digite aqui: '))
qtd = int(input('quantos: '))

if bebida == 1:
    preco = qtd * 6.00
    print(f'o valor de {qtd} refirgerante(s) é de R${preco:.2f}')
elif bebida == 2:
    tipo = int(input('se for de uva digite 1\n'
                     'se for de laranja digite 2\n'
                     'digite aqui:'))
    preco = qtd * 18.90
    if tipo == 1:
        print(f'o valor de {qtd} suco(s) de uva é de R${preco:.2f}')
    elif tipo == 2:
        print(f'o valor de {qtd} suco(s) de laranja é de R${preco:.2f}')


else:
    print('opção invalida')
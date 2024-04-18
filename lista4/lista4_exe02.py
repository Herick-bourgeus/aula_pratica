""" Faça um programa que pergunte ao usuário o que ele deseja comer: pizza, hambúrguer
ou salada. Se escolher pizza ou hambúrguer, pergunte se ele quer refrigerante. Informe o
preço total considerando que o refrigerante custa adicionalmente R$ 5,00. O valor da pizza,
do hambúrguer e da salada é o mesmo: R$39,90. Não esqueça de perguntar a quantidade
de cada item.
"""

opc = int(input('se deseja  comer pizza digite 1. \n '
                'se deseja comer hambúrguer digite digite 2. \n'
                'se deseja comer salada digite 3. \n'
                '\n'
                'digite aqui:'))

if opc == 1:
    qtd_pizzas = int(input('quantas pizzas você quer: '))

    preco_pizza = 39.90 * qtd_pizzas

    refrigerante = int(input('você deseja refigerante. \n'
                             'se sim digite 1. \n'
                             'se não digite 2. \n'
                             '\n'
                             'digte aqui:'))

    if refrigerante == 1:
        qtd_refrigerantes = int(input('quantos refigerantes você quer: '))
        preco_refigerantes = qtd_refrigerantes * 5
        preco_total = preco_pizza + preco_refigerantes
        print('o valor de', qtd_pizzas, 'pizza +', qtd_refrigerantes,' refrigerante é de R$', preco_total)

    elif refrigerante == 2:
        print('o valor de', qtd_pizzas, 'pizza é de R$', preco_pizza)


if opc == 2:
    qtd_hamburguer = int(input('quantos hambúrgueres você quer: '))

    preco_hamburguer = 39.90 * qtd_hamburguer

    refrigerante = int(input('você deseja refigerante. \n'
                             'se sim digite 1. \n'
                             'se não digite 2. \n'
                             '\n'
                             'digte aqui:'))

    if refrigerante == 1:
        qtd_refrigerantes = int(input('quantao refigerantes você quer: '))
        preco_refigerantes = qtd_refrigerantes * 5
        preco_total = preco_hamburguer + preco_refigerantes
        print('o valor de',qtd_hamburguer,' hambúrguer +', qtd_refrigerantes,'refrigerante é de R$',preco_total)

    elif refrigerante == 2:
        print('o valor de', qtd_hamburguer, 'é de R$', preco_hamburguer)


elif opc == 3:
    qtd_saladas = int(input('quantas saladas você quer: '))
    preco_total = qtd_saladas * 39.90
    print('o valor de',qtd_saladas,' salada é de R$ ', preco_total)

else:
    print('opção invalida')

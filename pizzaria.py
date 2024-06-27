"""Faça um algoritmo para calcular a conta de um número
indefinido de mesas de uma pizzaria.
Considere que o usuário possa informar através de um menu
os seguintes itens:
As bebidas e as quantidades vendidas
As pizzas e as quantidades vendidas
As sobremesas e as quantidades vendidas
No final do processamento (no final do cálculo de todas
as contas das mesas)
as seguintes informações devem ser impressas:
a. A maior e a menor conta
b. A média de gasto por mesa
c. A média de gasto por pessoa
d. A média de pizzas consumida por mesa
e. A média de pedaços de pizzas consumidas por pessoas
f. A média de bebidas consumidas por mesas"""

mesas = []
mesa_numero = 1
while True:
    bebida_preco = 6.00
    pizza_preco = 39.90
    sobremesa_preco = 10.00
    qtd_bebidas = 0
    qtd_pizzas = 0
    qtd_sobremesas = 0
    pessoas = 0

    print(f"Informe os itens consumidos pela mesa {mesa_numero}:")
    while True:
        print("1. Adicionar bebida")
        print("2. Adicionar pizza")
        print("3. Adicionar sobremesa")
        print("4. finalizar conta da mesa")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            quantidade = int(input("Quantas Bebidas?"))
            qtd_bebidas += quantidade
        elif opcao == 2:
            quantidade = int(input("Quantas pizzas?"))
            qtd_pizzas += quantidade
        elif opcao == 3:
            quantidade = int(input("Quantas dobremesa?"))
            qtd_sobremesas += quantidade
        elif opcao == 4:
            quantidade = int(input("Quantas pessoas na mesa?"))
            break
        else:
            print("Opçao invalida, tente novamente")

    total_conta =(qtd_bebidas * bebida_preco + qtd_pizzas * pizza_preco + qtd_sobremesas * sobremesa_preco)
    mesas.append((mesa_numero, total_conta, pessoas, qtd_pizzas, qtd_bebidas, qtd_sobremesas))

    print(f"\nRelatório da mesa {mesa_numero}:")
    print(f"Bebidas: {qtd_bebidas} x R${bebida_preco:.2f} = R${qtd_bebidas * bebida_preco:.2f}")
    print(f"Pizzas: {qtd_pizzas} x R${pizza_preco:.2f} = R${qtd_pizzas * pizza_preco:.2f}")
    print(f"Sobremesas: {qtd_sobremesas} x R${sobremesa_preco:.2f} = R${qtd_sobremesas * sobremesa_preco:.2f}")
    print(f"Total da conta: R${total_conta:.2f}\n")

    mais_mesas = input("Deseja adicionar outra mesa? (s/n) ")
    if mais_mesas.lower() != 's':
        break

    mesa_numero += 1

maior_conta = -1
menor_conta = float('inf')
total_gasto = 0
total_pessoas = 0
total_pizzas = 0
total_bebidas = 0
total_sobremesas = 0

i = 0
while i < len(mesas):
    mesa_numero = mesas[i][0]
    conta = mesas[i][1]
    pessoas = mesas[i][2]
    qtd_pizzas = mesas[i][3]
    bebidas = mesas[i][4]
    qtd_sobremesas = mesas[i][5]

    if conta > maior_conta:
        maior_conta = conta
        mesa_maior_conta = mesa_numero
    if conta < menor_conta:
        menor_conta = conta
        mesa_menor_conta = mesa_numero

    total_gasto = total_gasto + conta
    total_pessoas = total_pessoas + pessoas
    total_pizzas = total_pizzas + qtd_pizzas
    total_bebidas = total_bebidas + bebidas
    total_sobremesas = total_sobremesas + qtd_sobremesas

    i += 1

media_gasto_mesa = total_gasto / len(mesas)
media_gasto_pessoa = total_gasto / total_pessoas
media_pizzas_mesa = total_pizzas / len(mesas)
media_pedacos_pessoa = (total_pizzas * 8) / total_pessoas  # Considerando que cada pizza tem 8 pedaços
media_cervejas_mesa = total_bebidas / len(mesas)

print(f"Maior conta: R${maior_conta:.2f} (Mesa {mesa_maior_conta})")
print(f"Menor conta: R${menor_conta:.2f} (Mesa {mesa_menor_conta})")
print(f"Média de gasto por mesa: R${media_gasto_mesa:.2f}")
print(f"Média de gasto por pessoa: R${media_gasto_pessoa:.2f}")
print(f"Média de qtd_pizzas consumidas por mesa: {media_pizzas_mesa:.2f}")
print(f"Média de pedaços de pizza consumidos por pessoa: {media_pedacos_pessoa:.2f}")
print(f"Média de cervejas consumidas por mesa: {media_cervejas_mesa:.2f}")
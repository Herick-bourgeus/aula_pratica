"""Utilizando estrutura de decisão, crie um programa que lê como entrada o preço de um
produto e o código relativo à forma de pagamento. De acordo com a tabela dada abaixo,
eve ser aplicado o desconto especificado e o programa deve exibir o número de
prestações e o valor de cada prestação a ser paga:
"""

preco = float(input("Digite o preço do produto: "))
codigo = int(input("Digite o codigo da forma de pagamento: "))

if codigo == 1:
    pagar = preco * 0.7
    print("você obteve um desconto de 30%")
    print(f"você pagara a vista um valor de R${pagar:.2f}")
elif codigo == 2:
    pagar = preco * 0.8
    parcela = pagar / 2
    print("você obteve um desconto de 20%")
    print(f"você ira pagar duas parcelas de R${parcela:.2f},totalizando R${pagar:.2f} ")
elif codigo == 3:
    pagar = preco * 0.9
    parcela = pagar / 3
    print("você obteve um desconto de 10%")
    print(f"vocêe ira pagar três parcelas de R${parcela:.2f},totalizando R${pagar:.2f} ")
elif codigo == 4:
    qtd_parcelas = int(input("quer divir em quantas vezes:"))
    parcela = preco / qtd_parcelas


    print(f"vocêe ira pagar {qtd_parcelas} parcelas de R${parcela:.2f},totalizando R${preco:.2f} ")
else:
    print("codigo invalido")
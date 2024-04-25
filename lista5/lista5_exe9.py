"""Implemente um programa que lê como entrada o preço de custo de um produto e o
código relativo à categoria do produto. De acordo com a tabela dada a seguir, deve ser
calculado o preço de venda do produto, levando em conta a margem de lucro calculada
sobre o preço de custo do produto:"""

preco = float(input("qual o valor do produto: "))
codigo = int(input("digite o codigo relativo a categoria do produto: "))

if codigo == 1:
    pagar = (preco * 0.8) + preco
    print("voce escolheu hortifruti")
    print(f"você ira pagar o valor de R${pagar:.2f}")
elif codigo == 2:
    pagar = (preco * 0.8) + preco
    print("voce escolheu laticíneos")
    print(f"você ira pagar o valor de R${pagar:.2f}")
elif codigo == 3:
    pagar = (preco * 1) + preco
    print("voce escolheu carnes")
    print(f"você ira pagar o valor de R${pagar:.2f}")
elif codigo == 4:
    pagar = (preco * 1) + preco
    print("voce escolheu peixes")
    print(f"você ira pagar o valor de R${pagar:.2f}")
elif codigo == 5:
    pagar = (preco * 0.9) + preco
    print("voce escolheu aves")
    print(f"você ira pagar o valor de R${pagar:.2f}")
elif codigo == 6:
    pagar = (preco * 0.9) + preco
    print("voce escolheu ovos")
    print(f"você ira pagar o valor de R${pagar:.2f}")

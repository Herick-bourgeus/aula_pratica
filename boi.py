boi = 0
soma_pesos = 0
gordo = 0
magro = float('inf')
cont = 0
boi_mais_magro = []
boi_mais_gordo = []

boi = int(input("Digite a quantidade de bois: "))

while cont < boi:
    n = int(input(f"\nDigite o numero do boi {cont + 1}:"))

    peso = float(input("Dgite o peso do boi (em kg): "))

    somas_pesos = soma_pesos + peso

    if peso > gordo:
        gordo = peso
        boi_mais_gordo = [n]
    elif peso == gordo:
        boi_mais_gordo.append(n)

    if peso < boi:
        magro = peso
        boi_mais_magro.append(n)
    elif peso == magro:
        boi_mais_magro.append(n)

    cont += 1


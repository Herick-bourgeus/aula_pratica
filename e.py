pessoas = 0
cont = 0
idade = 0
soma_idades = 0
idade_maior = 0
idade_menor = 120
castanho = 0
preto = 0
loiro = 0
outro = 0
altura_170 = 0
peso_80 = 0
feminino = 0
masculino = 0

pessoas_valida = False

while pessoas_valida == False:
    pessoas = int(input("digite a qunatidade de pessoas: "))

    if pessoas <= 0:
        print("quantidade invalida! Tente novamente.")
        input("precione Enter para continuar...")
    else:
        pessoas_valida = True

cont = 1
while cont <= pessoas:
    idade_valida = False
    while idade_valida == False:
        idade = int(input(f"digite a idade da {cont}ª pessoa: "))
        if idade <= 0 or idade > 120:
            print("quantidade invalida! Tente novamente. ")
            input("precione Enter para continuar...")
        else:
            idade_valida = True
    soma_idades = soma_idades + idade
    if idade >= 18:
        maioridade = maioridade + 1
    if idade >= idade_maior:
        idade_maior = idade
    if idade <= idade_menor:
        idade_menor = idade

    cabelo_valido = False
    while cabelo_valido == False:
        print(f"Digite a opção que corresponde à cor do cabelo da {cont}ª pessoa:")
        print("1 - Castanho\n2 - Preto\n3 - Loiro\n4 - Outro")
        cabelo = int(input("Opção: "))
        if cabelo < 1 or cabelo > 4:
            print("Opção inválida! Tente novamente.")
            input("Pressione Enter para continuar...")
        else:
            cabelo_valido = True
    if cabelo == 1:
        castanho += 1
    elif cabelo == 2:
        preto += 1
    elif cabelo == 3:
        loiro += 1
    else:
        outro += 1

    altura_valida = False
    while altura_valida == False:
        altura = float(input(f"Digite a altura da {cont}ª pessoa em metros: "))
        if altura <= 0.30 or altura > 2.50:
            print("Altura inválida! Tente novamente.")
            input("Pressione Enter para continuar...")
        else:
            altura_valida = True
    if altura > 1.70:
        altura_170 += 1

    peso_valido = False
    while peso_valido == False:
        peso = float(input(f"Digite o peso da {cont}ª pessoa: "))
        if peso <= 0 or peso > 400:
            print("Peso inválido! Tente novamente.")
            input("Pressione Enter para continuar...")
        else:
            peso_valido = True
    if peso > 80:
        peso_80 += 1

    sexo_valido = False
    while sexo_valido == False:
        print(f"Digite a opção que corresponde ao sexo da {cont}ª pessoa:")
        print("1 - Feminino\n2 - Masculino")
        sexo = int(input("Opção: "))
        if sexo != 1 and sexo != 2:
            print("Opção inválida! Tente novamente.")
            input("Pressione Enter para continuar...")
        else:
            sexo_valido = True

    if sexo == 1:
        feminino += 1
    else:
        masculino += 1
    cont =+ 1



"""
if maioridade > 0:
    print(f"A quantidade de pessoas que possuem idade superior a 18 anos é: {maioridade}")
print(f"A média de idade é {media_idades:.2f} anos")
print(f"A maior idade entre os entrevistados é {idade_maior}")
print(f"A menor idade entre os entrevistados é {idade_menor}")
if porcentagem_castanho > 0:
    print(f"A porcentagem de pessoas com cabelo castanho é: {porcentagem_castanho:.2f}%")
if porcentagem_preto > 0:
    print(f"A porcentagem de pessoas com cabelo preto é: {porcentagem_preto:.2f}%")
if porcentagem_loiro > 0:
    print(f"A porcentagem de pessoas com cabelo loiro é: {porcentagem_loiro:.2f}%")
if porcentagem_outro > 0:
    print(f"A porcentagem de pessoas com cabelo de outra cor é: {porcentagem_outro:.2f}%")
if altura_170 > 0:
    print(f"A quantidade de pessoas que possuem altura maior que 1.70 m é: {altura_170}")
if peso_80 > 0:
    print(f"A quantidade de pessoas que possuem peso superior a 80 quilos é: {peso_80}")
if porcentagem_feminino > 0:
    print(f"A porcentagem de pessoas do sexo feminino é: {porcentagem_feminino:.2f}%")
if porcentagem_masculino > 0:
    print(f"A porcentagem de pessoas do sexo masculino é: {porcentagem_masculino:.2f}%")"""
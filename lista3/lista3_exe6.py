

num1 = float(input("Digite um numero: "))
num2 = float(input("Digite outro numero: "))

opc = input("digite 1 para saber a media entre os dois numeros. \n"
            "digite 2 para saber a diferença do maior para o menor. \n"
            "digite 3 para saber o produto entre os dois numeros. \n"
            "digite aqui : ")

if opc == "1":
    media = (num1 + num2) / 2
    print("A media entre os dois numeros é: ", media)
elif opc == "2":
    if num1 < num2:
        diferença = num2 - num1
        print("A diferença entre os dois numeros é", diferença)
    else:
        diferença = num1 - num2
        print("a diferença entre os dois numeros é ", diferença)
elif opc == "3":
    produto = num1 * num2
    print("O produto entre eles é ", produto)
else:
    print("opção invalida")
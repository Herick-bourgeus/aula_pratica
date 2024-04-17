

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o Segundo numero: '))

opc = int(input('digite 1 para saber a media entre os dois numeros.\n'
                'digite 2 para saber a diferença do maior pelo menor.\n'
                'digite 3 para saber o produto entre os dois numeros.\n'
                'digite 4 para saber a divisao entre os dois numeros.\n'
                'digite aqui: '))

if opc == 1:
    media = (num1 + num2) / 2
    print('a media entre os dois numeros é ', media)

elif opc == 2:
    if num1 > num2:
        diferenca = num1 - num2
        print('a diferença entre os dois numeros é ', diferenca)
    else:
        diferenca = num2 - num1
        print('a diferença entre os dois numeros é', diferenca)
elif opc == 3:
    produto = num1 * num2
    print('o produto entre os dois numeros é', produto)
elif opc == 4:
    if num2 != 0:
        divisao = num1 / num2
        print('a divisão entre os dois numeros é', divisao)
    else:
        print('é imposivel dividir por zero')


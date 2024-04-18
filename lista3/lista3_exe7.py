
salario = float(input("Digite o valor do seu salario: "))


if salario <= 500:
    aumento = salario + (salario * 0.30)
    print("voce tem direito ao aumento.\n"
          "\n"
          "Seu salario atual é de R$", aumento)
else:
    print("voce não tem direito ao aumento de 30%")
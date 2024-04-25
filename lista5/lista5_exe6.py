"""Construir um programa para identificar quantos dias há em um mês, sabendo o mês e o
ano.
"""

mes = int(input("Digite o número do mês (1-12): "))
ano = int(input("Digite o ano: "))

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    print(f"O mês {mes} do ano {ano} tem 31 dias.")
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print(f"O mês {mes} do ano {ano} tem 30 dias.")
elif mes == 2:
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        print(f"O mês {mes} do ano {ano} tem 29 dias (ano bissexto).")
    else:
        print(f"O mês {mes} do ano {ano} tem 28 dias.")
else:
    print("Mês inválido.")

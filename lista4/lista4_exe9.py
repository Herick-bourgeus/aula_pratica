"""Crie um programa que pergunte ao usuário se ele é sócio do clube. Se sim, permita
acesso. Se não, informe que é necessário ser sócio para entrar ao local.
"""

socio = input("Você é sócio do clube? \n"
              "se sim tecle 1\n"
              "se não tecle 2\n"
              "\n"
              "digite aqui: ")

if socio == 1:
    print("Acesso permitido.")
elif socio == 2:
    print("Desculpe, é necessário ser sócio para entrar no local.")
else:
    print("opção invalida ")

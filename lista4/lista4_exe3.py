"""Crie um programa que define uma senha (por exemplo, "Abc123"). Peça ao usuário para
digitar uma senha e verifique se ela está correta. Informe ao usuário se ele acertou ou
errou.
"""

senha = input("crie uma senha: ")
senha2 = input("digite a senha novamente: ")
if senha2 == senha:
    print("Acesso Permitido")
else:
    print("Acesso negado")
""" Crie um programa que solicita ao usuario todos os dados necessarios para realizar um cadastro no IFSP Rio Preto"""

nome = input('Digite seu nome: ')
idade = input("Digite sua data de nascimento (DD/MM/AAAA): ")
cpf = input('Digite seu CPF: ')
endereco = input('Digite seu endereco: ')
curso = input('Digite seu curso: ')

#Confirmacao dos dados inseridos
print("\nConfirmacao de Cadastro:")
print("nome :  ", nome )
print("idade : ", idade )
print("cpf : ", cpf )
print("endereco : ", endereco )
print("curso : ", curso )

print("\nSeus dados foram recebidos com sucessos!!!")


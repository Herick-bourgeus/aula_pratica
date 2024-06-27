"""Para eleição de representantes de classe de uma
universidade há três candidatos.
Os votos são informados através de código:
1,2 ou 3, voto para os respectivos candidatos, 5 voto nulo e 6 voto em branco.
Faça um algoritmo que calcule e escreva:
a. A porcentagem e o total de votos para cada candidato
b. Total de votos nulos
c. Total de votos em branco
d. Percentual de votos em brancos e nulos
e. Classificação dos candidatos
f. Total de votos"""






# Variáveis necessárias
total_votos = 0
votos_candidato1 = 0
votos_candidato2 = 0
votos_candidato3 = 0
votos_nulos = 0
votos_brancos = 0

print("Digite o código do voto (1, 2, 3 para candidatos; 5 para nulo; 6 para branco; 0 para finalizar):")

while True:
    voto = (input("Digite o voto: "))
    if voto == "0":
        break
    total_votos = total_votos + 1
    if voto == "1":
        votos_candidato1 = votos_candidato1 + 1
    elif voto == "2":
        votos_candidato2 = votos_candidato2 + 1
    elif voto == "3":
        votos_candidato3 = votos_candidato3 + 1
    elif voto == "5":
        votos_nulos = votos_nulos + 1
    elif voto == "6":
        votos_brancos = votos_brancos + 1
    else:
        print("numero invalido")


# Calculando porcentagens de cada candidato:
percentual_candidato1 = (votos_candidato1 / total_votos) * 100
percentual_candidato2 = (votos_candidato2 / total_votos) * 100
percentual_candidato3 = (votos_candidato3 / total_votos) * 100
percentual_nulos = (votos_nulos / total_votos) * 100
percentual_brancos = (votos_brancos / total_votos) * 100

# Total de Votos
print(f"teve {total_votos} votos")

# Classificação

if votos_candidato1 > votos_candidato2 and votos_candidato1 > votos_candidato3:
    if votos_candidato2 > votos_candidato3:
        print(f"O candidato 1 teve maior quantidade de votos! ")
        print(f"O candidato 2 ficou em segundo e o candidato 3 ficou em terceiro lugar! ")
    else:
        print(f"O candidato 1 teve maior quantidade de votos! ")
        print(f"O candidato 3 ficou em segundo e o candidato 2 ficou em terceiro lugar! ")
elif votos_candidato2 > votos_candidato1 and votos_candidato2 > votos_candidato3:
    if votos_candidato1 > votos_candidato3:
        print(f"O candidato 2 teve maior quantidade de votos! ")
        print(f"O candidato 1 ficou em segundo e o candidato 3 ficou em terceiro lugar! ")
    else:
        print(f"O candidato 2 teve maior quantidade de votos! ")
        print(f"O candidato 3 ficou em segundo e o candidato 1 ficou em terceiro lugar! ")
elif votos_candidato3 > votos_candidato1 and votos_candidato3 > votos_candidato2:
    if votos_candidato2 > votos_candidato1:
        print(f"O candidato 3 teve maior quantidade de votos! ")
        print(f"O candidato 2 ficou em segundo e o candidato 1 ficou em terceiro lugar! ")
    else:
        print(f"O candidato 3 teve maior quantidade de votos! ")
        print(f"O candidato 1 ficou em segundo e o candidato 1 ficou em terceiro lugar! ")

# Resultados
print("\nResultados da Votação:")
print(f"Total de votos: {total_votos}")
print(f"Candidato 1: {votos_candidato1} votos ({percentual_candidato1:.2f}%)")
print(f"Candidato 2: {votos_candidato2} votos ({percentual_candidato2:.2f}%)")
print(f"Candidato 3: {votos_candidato3} votos ({percentual_candidato3:.2f}%)")
print(f"Votos nulos: {votos_nulos} votos ({percentual_nulos:.2f}%)")
print(f"Votos em branco: {votos_brancos} votos ({percentual_brancos:.2f}%)")
print(f"Percentual de votos em branco e nulos: {(percentual_brancos + percentual_nulos):.2f}%")
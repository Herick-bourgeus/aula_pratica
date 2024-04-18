"""Escreva um programa que pergunte ao usuário a hora atual (somente a hora, sem os
minutos) e se hoje é um dia útil ou fim de semana. Se for antes das 22h em dia útil, informe
que ainda é cedo para dormir. Se for fim de semana ou após as 22h, diga que é um bom
horário para dormir."""

hora_atual = int(input("Que horas são agora? (Digite apenas a hora, sem minutos) "))
dia_util = input("Hoje é um dia útil?\n"
                 "se sim digite 1\n"
                 "se não digite 2\n "
                 "\n"
                 "digite aqui:")

if dia_util == 1 and hora_atual < 22:
    print("Ainda é cedo para dormir.")
elif dia_util == 2 or hora_atual >= 22:
    print("É um bom horário para dormir.")
elif hora_atual < 22:
    print("Ainda não é hora de dormir.")
else:
    print("opção invalida")

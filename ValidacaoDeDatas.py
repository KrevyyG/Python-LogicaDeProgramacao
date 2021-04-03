print("Digite uma data, (Apenas Nºs)")
dia = int(input("Digite um Dia: "))
mes = int(input("Digite um Mês: "))
ano = int(input("Digite um Ano: "))

if dia > 28 and mes == 2:
    print("Data inválida")
elif dia > 30 and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
    print("Data inválida")
elif dia > 31 and (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
     print("Data inválida")
else:
    if mes > 12:
         print("Data inválida")
    else:
        print("Data Válida")
        print(dia,"/",mes,"/",ano)

dia = int(input("Digite o dia do seu aniversário: "))
mesN = int(input("Digite o mês do seu aniversário (número): "))

if mesN == 1 and dia <= 31:
    print("Sua data de aniversário é: ", dia, "de Janeiro")
elif mesN == 2 and dia <= 29:
    print("Sua data de aniversário é: ", dia, "de Fevereiro")
elif mesN == 3 and dia <= 31:
   print("Sua data de aniversário é: ", dia, "de Março")
elif mesN == 4 and dia <= 30:
   print("Sua data de aniversário é: ", dia, "de Abril")
elif mesN == 5 and dia <= 31:
    print("Sua data de aniversário é: ", dia, "de Maio")
elif mesN == 6 and dia <= 30:
    print("Sua data de aniversário é: ", dia, "de Junho")
elif mesN == 7 and dia <= 31:
    print("Sua data de aniversário é: ", dia, "de Julho")
elif mesN == 8 and dia <= 31:
    print("Sua data de aniversário é: ", dia, "de  Agosto")
elif mesN == 9 and dia <= 30:
    print("Sua data de aniversário é: ", dia, "de Setembro")
elif mesN == 10 and dia <= 31:
    print("Sua data de aniversário é: ", dia, "de Outubro")
elif mesN == 11 and dia <= 30:
    print("Sua data de aniversário é: ", dia, "de Novembro")
elif mesN == 12 and dia <= 31:
    print("Sua data de aniversário é: ", dia, "de Desembro")
else:
    print("Data inválida")

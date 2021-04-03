salM = float(input("Digite a quantia do sálario (Mensal): R$ "))
salA = salM * 12
if salA >= 22847.77 and salA <= 33919.80:
    aliq =  round((salA * 7.5)/100, 2)
    print("O valor do imposto de renda a ser recolhido é referente a 7,5% do salário (Anual) digitado.")
    print("Valor:  R$ ", aliq)
elif salA >= 33919.81 and salA <=  45012.60:
    aliq = round((salA * 15)/100, 2)
    print("O valor do imposto de renda a ser recolhido é referente a 15% do salário (Anual) digitado.")
    print("Valor: ",  aliq)
elif salA >= 45012.61 and salA <=  55976.16:
    aliq = round((salA * 22.5)/100, 2)
    print("O valor do imposto de renda a ser recolhido é referente a 22,5% do salário (Anual) digitado")
    print("Valor: ",  aliq)
elif salA >= 55976.17:
    aliq = round((salA * 27.5)/100, 2)
    print("O valor do imposto de renda a ser recolhido é referente a 27,5% do salário (Anual) digitado")
    print("Valor: ",  aliq)
else:
    print("Você é isento do valor de imposto de renda a ser recolhido")

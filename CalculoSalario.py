hrsM=int(input("Digite a quantidade de horas trabalhadas no mês: "))
salH=float(input("Digite o salário por hora: R$ "))
hrsS= hrsM/4

if hrsS > 40:
    salS=salH*hrsS
    hrsEx=hrsM%40
    salHEx=(salH*50)/100
    salMEx=salHEx*hrsEx
    salM=salS*4
    salT=salMEx + salM
    print("Seu salário Mensal + Hora Extras, será de: R$ ",salT)
else:
    salS=salH*hrsS
    salM=salS*4
    print("Seu salário Mensal será de: R$ ",salM)

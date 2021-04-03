sexo = input("Selecione seu sexo digitando F/M: ")
h = float(input("Digite sua altura: "))

if sexo == "F":
    p = int(20.8 * h**2)
    print ("Seu peso ideal é: ", p,"Kg")
else:
    p = int(22.0 * h**2)
    print ("Seu peso ideal é: ", p,"Kg")

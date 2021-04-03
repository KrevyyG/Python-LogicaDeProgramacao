hE = int(input ("Digite a Hora de entrada: "))
mE =  int(input ("Digite os minutos de entrada: "))
hS =  int(input ("Digite a Hora de saída: "))
mS =  int(input ("Digite os minutos de saída: "))
minE = mE + (60 * hE)
minS = mS + (60 * hS)
duracao = minS - minE

if duracao < 0:
    print("Horario inválido")
else:
    print("A duração de permanencia no estacionamento foi de", duracao, " minutos")

    

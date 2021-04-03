t1=input("Digite o nome do primeiro time: ")
p1=int(input("Digite os pontos do primeiro time: "))
t2=input("Digite o nome do segundo time: ")
p2=int(input("Digite os pontos do segundo time: "))
t3=input("Digite o nome do terceiro time: ")
p3=int(input("Digite os pontos do terceiro time: "))

if p1 > p2 and p1 > p3 and p2 > p3:
    print ("1º lugar: ", t1)
    print ("2º lugar: ", t2)
    print ("3º lugar: ", t3)
elif p1> p2 and p1 > p2 and p3 > p2:
    print ("1º lugar: ", t1)
    print ("2º lugar: ", t3)
    print ("3º lugar: ", t2)
elif p1> p2 and p1 > p2 and p3 > p2:
    print ("1º lugar: ", t1)
    print ("2º lugar: ", t3)
    print ("3º lugar: ", t2)
elif  p2 > p1 and p2 > p3 and p1 > p3:
    print ("1º lugar: ", t2)
    print ("2º lugar: ", t1)
    print ("3º lugar: ", t3)
elif p1> p2 and p1 > p2 and p3 > p2:
    print ("1º lugar: ", t2)
    print ("2º lugar: ", t3)
    print ("3º lugar: ", t1)
elif p3> p1 and p3 > p2 and p1 > p2:
    print ("1º lugar: ", t3)
    print ("2º lugar: ", t1)
    print ("3º lugar: ", t2)
elif p3> p1 and p3 > p2 and p1 > p2:
    print ("1º lugar: ", t3)
    print ("2º lugar: ", t2)
    print ("3º lugar: ", t1)
elif p1 == p2 and p1 > p3:
    print("Ouve um empate")
    print ("1º lugar: ", t1, " e ",t2)
    print ("2º lugar: ", t3)
elif p1 == p3 and p1 > p2:
    print("Ouve um empate")
    print ("1º lugar: ", t1, " e ",t3)
    print ("2º lugar: ", t2)
elif p2 == p3 and p2 > p1:
    print("Ouve um empate")
    print ("1º lugar: ", t2, " e ",t3)
    print ("2º lugar: ", t1)
else:
    print("Ouve um empate")
    print ("1º lugar: ", t1, ", ",t2, " e ", t3)






    

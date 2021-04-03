print("Nºs Jogados")
n1=int(input("Digite o primeiro Nº jogado: "))
n2=int(input("Digite o segundo Nº jogado: "))
n3=int(input("Digite o terceiro Nº jogado: "))
n4=int(input("Digite o quarto Nº jogado: "))
n5=int(input("Digite o quinto Nº jogado: "))
n6=int(input("Digite o sexto Nº jogado: "))

print("Nºs Sorteados")
ns1=int(input("Digite o primeiro Nº sorteado: "))
ns2=int(input("Digite o segundo Nº sorteado: "))
ns3=int(input("Digite o terceiro Nº sorteado: "))
ns4=int(input("Digite o quarto Nº sorteado: "))
ns5=int(input("Digite o quinto Nº sorteado: "))
ns6=int(input("Digite o sexto Nº sorteado: "))

nr = 0

if ns1 == n1 or ns1 == n2  or ns1 == n3 or ns1 == n4 or ns1 == n5 or ns1 == n6:
    nr = nr + 1
else:
    nr = nr
if ns2 == n1 or ns2 == n2  or ns2 == n3 or ns2 == n4 or ns2 == n5 or ns2 == n6:
   nr = nr + 1
else:
    nr = nr
if ns3 == n1 or ns3 == n2  or ns3 == n3 or ns3 == n4 or ns3 == n5 or ns3 == n6:
   nr = nr + 1
else:
    nr = nr
if ns4 == n1 or ns4 == n2  or ns4 == n3 or ns4 == n4 or ns4 == n5 or ns4 == n6:
   nr = nr + 1
else:
    nr = nr
if ns5 == n1 or ns5 == n2  or ns5 == n3 or ns5 == n4 or ns5 == n5 or ns5 == n6:
   nr = nr + 1
else:
    nr = nr
if ns6 == n1 or ns6 == n2  or ns6 == n3 or ns6 == n4 or ns6 == n5 or ns6 == n6:
   nr = nr + 1
else:
    nr = nr

if nr == 0:
    print("Você não acertou nenhum número.")
elif nr == 1:
    print("Você acertou apenas um número.")
elif nr == 2:
    print("Você acertou apenas dois  números.")
elif nr == 3:
    print("Você acertou três números.")
elif nr == 4:
    print("Você acertou a quadra !")
elif nr == 5:
    print("Você acertou a quina !")
else:
    print("Você acertou a sena !")

print(nr)

resposta = "S" or "s"


while resposta == "S" or resposta == "s":
    cont = 0
    nomeM = " "
    salarioM =  0

    while cont < 10:
        cont = cont + 1
        nome = input("Digite o nome do Funcionário: ")
        salario = float(input("Digite o Salário desse funcionário: R$ "))
        if salario > salarioM:
            salarioM = salario
            nomeM = nome
            
    print("O Funcionário", nomeM, "possui o maior salário (R$ ", salarioM,")")
    resposta = str(input("Deseja reiniciar o programa ? (S/N): "))
    
else:
    print("Sistema finalizado")


        

        

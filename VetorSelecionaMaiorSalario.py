nomes = []
salario = []

for i in range (3):
    nomes.append(input("Digite o nome do funcionário: "))
    salario.append(float(eval(input("Digite o salário do funcionário " + nomes[i] + ": R$"))))

print("O Funcionário que ganha mais  é:")
for i in range (len(salario)):
    if  salario[i]  >  salario[i] :
        salarioM = salario[i]
        print (nomes[i], "com salário de R$", salarioM)
        
print("O Funcionário que ganha abaixo de R$1000 é:")
for i in range (len(nomes)):
    if salario[i] < 1000:
        print(nomes[i])

base = int(input("Digite um número como base de uma potência: "))
exp = int(input("Digite um número como expoente de uma potência: "))

cont = 1
soma = 1

while cont <= exp:
    soma = soma * base
    cont  = cont + 1
    
print (soma)

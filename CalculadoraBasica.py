n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
op = input ("""Digite os respectivos sinais para realizar uma operação
Soma "+"
Subtração "-"
Multiplicação "x"
Divisão "/"
Qual operação deseja fazer ?: """)

if op == "+":
    result = n1+ n2
    print(n1," + ",n2," = ", result)
elif op == "-":
    result = n1 - n2
    print(n1," - ",n2," = ", result)
elif op == "x" or op == "X":
    result = n1 * n2
    print(n1," x ",n2," = ", result)
elif op == "/":
    result = n1 / n2
    print(n1," / ",n2," = ", result)
else:
    print("Operação inválida")
    

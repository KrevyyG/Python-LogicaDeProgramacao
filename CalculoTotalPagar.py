esp=int(input("Digite a especificação ou código do pedido: "))
quant = int(input("Quantos produtos deseja comprar: "))

if esp == 100:
    total = 2.10*quant
    print("O total a pagar é: ",total)
elif esp == 101:
    total = 3.00*quant
    print("O total a pagar é: ", total)
elif esp == 102:
    total = 4.00*quant
    print("O total a pagar é: ",total)
else:
    print("Esp Inval")

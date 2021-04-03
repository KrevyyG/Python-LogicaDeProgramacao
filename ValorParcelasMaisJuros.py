valor =  float(input("Digite o valor total da compra: "))
parc =  int(input("Opções de parcelas: 2x, 4x, 6x e 8x \n Digite a quantidade de parcelas desejadas: "))

if parc == 2:
    juros = (valor * 3)/100
    VlrParc = (valor + juros) / parc
    total = valor + juros
    print("Valor de juros a pagar  = R$ ", juros)
    print("2x de  R$ ",VlrParc)
    print("Valor total a pagar =  R$ ", total)
elif parc == 4:
    juros = (valor * 7)/100
    VlrParc = (valor + juros) / parc
    total = valor + juros
    print("Valor de juros a pagar  = R$ ", juros)
    print("4x de  R$ ",VlrParc)
    print("Valor total a pagar =  R$ ", total)
elif parc == 6:
     juros = (valor * 9)/100
     VlrParc = ((valor + juros) / parc)
     total = valor + juros
     print("Valor de juros a pagar  = R$ ", juros)
     print("6x de  R$ ",VlrParc)
     print("Valor total a pagar =  R$ ", total)
elif parc == 8:
     juros = (valor * 12)/100
     VlrParc = (valor + juros) / parc
     total = valor + juros
     print("Valor de juros a pagar  = R$ ", juros)
     print("8x de  R$ ",VlrParc)
     print("Valor total a pagar =  R$ ", total)
else:
    print("Parcela inválida")

preco = float(input("Valor da quantia gasta: R$ " ))


desc = (preco * 10) / 100
final = round(preco - desc, 2)
print("Valor de desconto (10%): R$", desc)
print("Valor a pagar: R$", final)


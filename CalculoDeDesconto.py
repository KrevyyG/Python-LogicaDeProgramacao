preco = float(input("Valor da quantia gasta: R$ " ))

if preco >= 200:
    desc = preco * (20/100)
    final = preco * (80/100)
    print("Valor de desconto: R$", desc)
    print("Valor a pagar: R$", final)
else:
    print("Valor a pagar: R$", preco)

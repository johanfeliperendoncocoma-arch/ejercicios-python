valor_compra = float(input("Ingresa el valor de la compra: "))
if valor_compra < 50000:
    descuento = 0.05
elif valor_compra <= 100000:
    descuento = 0.10
else:
    descuento = 0.15
valor_descuento = valor_compra * descuento
valor_final = valor_compra - valor_descuento
print(f"Descuento aplicado: {descuento * 100}%")
print(f"Valor del descuento: ${valor_descuento:.2f}")
print(f"Valor final a pagar: ${valor_final:.2f}")

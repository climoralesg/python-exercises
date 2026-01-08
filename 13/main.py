#13	Calcula un descuento según porcentaje.
price = float(input("Ingresa el precio: "))
discount = float(input("Ingresa el descuento "))

finalPrice = price*(1-discount/100)

print(f"El precio final con descuento es {finalPrice:.0f}")
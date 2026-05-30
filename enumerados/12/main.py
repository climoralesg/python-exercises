#12	Calcula el precio final con IVA.

price = float(input("Ingresa el precio de algo: "))

ivaPrice = price * 0.19

finalPrice = ivaPrice + price

print(f"El precio final con IVA es ${finalPrice:.2f}")
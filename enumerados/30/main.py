#30	Aplica descuento solo si el monto supera cierto valor.

valueLimit = 2000
price = int(input("Ingresa el precio"))
limit = int(input("Ingresa el precio de descuento"))

if valueLimit <= limit:
    result = price - limit
    print(f"El valor final es {result}")
else:
     print(f"El valor final es {price}")
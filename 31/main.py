#31	Determina si una edad está dentro de un rango válido.

number = int(input("Ingrese un numero: "))

rangeNumber = range(1,10)
print(f"{rangeNumber}")

if number in rangeNumber:
    print("Se encuentra en el rango")
else:
    print("No se encuentra en el rango")
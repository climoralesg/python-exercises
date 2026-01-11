#29	Determina si un año es bisiesto.

year = int(input("Ingrese un año "))

result = year % 4 == 0

if result:
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")


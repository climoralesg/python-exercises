#22	Determina si un número es positivo, negativo o cero.

number = int(input("Ingresa un valor: "))

if number == 0:
    print("El numero es 0")
else:
    if number > 0:
        print("El numero es positivo")
    else:
        print("El numero es negativo")
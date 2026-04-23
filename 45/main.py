#45	Valida entradas incorrectas.
while True:
    try:
        numero = int(input("Ingresa un número entero: "))
        print("Número válido:", numero)
        break
    except ValueError:
        print("Error: debes ingresar un número entero.")
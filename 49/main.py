#49	Muestra la tabla de multiplicar de un número dado.


try:
    number = int(input("Ingresa un numero: "))

    for i in range(0,11):
        result=number*i
        print(f"{number} x {i} = {result}")
except (ValueError, TypeError):
    print("Error en el tipo")



#24	Compara dos números e indica cuál es mayor o si son iguales.

numberFirst = int(input("Ingresa el primer numero: "))
secondNumber = int(input("Ingresa el segundo numero: "))

if numberFirst == secondNumber:
    print("Ambos numeros son iguales")
else:
    if numberFirst > secondNumber:
        print("El primer numero es mayor")
    else:
        print("El segundo numero es mayor")

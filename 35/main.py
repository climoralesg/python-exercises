#35	Determina si un número tiene uno, dos o tres dígitos.

number = int(input("Ingresa un numero "))

numberLetters = {
    1:"Uno",
    2:"Dos",
    3:"Tres",
}

numberToString = str(number)

numberCount = len(numberToString)

print(f"El numero ingresado tiene {numberLetters.get(numberCount,"Mas de 3")}")


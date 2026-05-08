#54	Invierte un número usando un bucle.

number = int(input("Ingresa un numero\n"))

numberString = str(number)

if numberString.isdigit():
    newWord = ""
    for i in range(len(numberString)-1,-1,-1):
        newWord=f"{newWord}{numberString[i]}"

    print(f"El numero al reves es {newWord}")
else :
    print("Ingrese numeros")

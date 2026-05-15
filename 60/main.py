#60	Valida entradas numéricas con while.

import random

randomNumber = random.randint(1,10)
print(f"Clave: {randomNumber}")
while True:
    number = input("Ingresa el numero\n")

    if number.isdigit():
        intNumber = int(number)
        if isinstance(intNumber,int) and intNumber == randomNumber:

            print("adivinaste!")
            break
        else:
            print("Incorrecto, intenta nuevamente")
    else:
        print("Fallaste, ingresa un numero")
#58	Juego de adivinar número con intentos.
import random

randomNumber = random.randint(1,10)
print(f"Clave: {randomNumber}")
while True:
    number = int(input("Ingresa el numero"))
    if number==randomNumber:
        print("adivinaste!")
        break
    else:
        print("Fallaste, intenta nuevamente")


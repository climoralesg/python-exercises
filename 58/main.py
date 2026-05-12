#58	Juego de adivinar número con intentos.
import random

attemps = 0
randomNumber = random.randint(1,10)
print(f"Clave: {randomNumber}")
while True:
    attemps +=1
    number = int(input("Ingresa el numero"))
    if number==randomNumber:
        print("adivinaste!")
        print(f"Numero de intentos {attemps}")
        break
    else:
        print("Fallaste, intenta nuevamente")


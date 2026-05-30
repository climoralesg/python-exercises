#32	Verifica si un número es múltiplo de 3 o de 5.

number = int(input("Ingresa un valor "))

mulFive = number % 5 == 0

mulThree = number % 3 == 0

print(f"{mulFive} {mulThree}")

if mulThree:
    print(f"El numero {number} es multiplo de 3")
elif mulFive:
    print(f"El numero {number} es multiplo de 5")
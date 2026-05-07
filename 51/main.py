#51	Calcula el factorial de un número.

number = int(input("Ingresa un numero para saber su factorial\n"))
acumAdd = 1
for i in range(1,number+1):
    tempValue = acumAdd
    acumAdd = acumAdd * i
    print(f"{tempValue} x {i} = {acumAdd}")

print(f"{number}! = {acumAdd}")